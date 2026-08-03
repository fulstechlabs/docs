# Migrate to Confluence Cloud

> **This migration step is ONLY necessary for the pre-4.0.0 versions of this app.**
>
> **If the Confluence Server or Data Center instance has never run a version older than 4.0.0, this migration process is not necessary.**

Since there are differences between rules for macro names between Confluence Cloud and Confluence Data Center/Server, the macro names have to be modified in the database before the migration to Confluence Cloud takes place.

The following guideline is based on an [Atlassian's article](https://confluence.atlassian.com/confkb/how-to-bulk-update-confluence-content-through-the-database-to-replace-old-macros-with-new-ones-1018780615.html). After finish all steps, you can follow this [Atlassian's migration guideline](https://support.atlassian.com/migration/docs/compare-cloud-migration-methods/) to import the data from Confluence Data Center/Server to Confluence Cloud.

## (Optional) Get a report on the pages using the macros

The following SQL query provides this information from the latest (current) version of pages using the old macros. This is targeting pages, blog posts, and page comments.

**LaTeX block** macro

#### PostgreSQL

```sql
SELECT c.contentid, c.contenttype, c.title, s.spacekey
FROM CONTENT c
JOIN BODYCONTENT bc
    ON c.contentid = bc.contentid
JOIN SPACES s
    ON c.spaceid = s.spaceid
WHERE c.prevver IS NULL
    AND c.contenttype IN ('PAGE', 'BLOGPOST', 'COMMENT')
    AND bc.body LIKE '%ac:name="LaTeX block"%';
```

**LaTeX inline** macro

#### PostgreSQL

```sql
SELECT c.contentid, c.contenttype, c.title, s.spacekey
FROM CONTENT c
JOIN BODYCONTENT bc
    ON c.contentid = bc.contentid
JOIN SPACES s
    ON c.spaceid = s.spaceid
WHERE c.prevver IS NULL
    AND c.contenttype IN ('PAGE', 'BLOGPOST', 'COMMENT')
    AND bc.body LIKE '%ac:name="LaTeX inline"%';
```

If [Collaborative editing](https://confluence.atlassian.com/doc/collaborative-editing-858771779.html) is enabled, we also need to touch the shared draft of target pages.\
The following SQL query provides information on shared drafts (pages and blog posts) using the old macro.

**LaTeX block** macro

#### PostgreSQL

```sql
SELECT c.contentid, c.contenttype, c.title, s.spacekey
FROM CONTENT c
JOIN BODYCONTENT bc
    ON c.contentid = bc.contentid
JOIN SPACES s
    ON c.spaceid = s.spaceid
WHERE c.content_status = 'draft'
    AND c.contenttype IN ('PAGE', 'BLOGPOST')
    AND bc.body LIKE '%ac:name="LaTeX block"%';
```

**LaTeX inline** macro

#### PostgreSQL

```sql
SELECT c.contentid, c.contenttype, c.title, s.spacekey
FROM CONTENT c
JOIN BODYCONTENT bc
    ON c.contentid = bc.contentid
JOIN SPACES s
    ON c.spaceid = s.spaceid
WHERE c.content_status = 'draft'
    AND c.contenttype IN ('PAGE', 'BLOGPOST')
    AND bc.body LIKE '%ac:name="LaTeX inline"%';
```

## Stop Confluence

Stop Confluence following your standard procedure. If running Confluence Data Center, stop Confluence on all nodes.

## Stop the Synchrony process

**If Collaborative Editing is enabled** and Synchrony is running on a [standalone cluster](https://confluence.atlassian.com/doc/set-up-a-synchrony-cluster-for-confluence-data-center-958779073.html), stop the Synchrony process on each node.

## Update data

### All necessary queries for easy copying-and-pasting

```sql
update CONTENTPROPERTIES
set stringval = 'synchrony-recovery'
where CONTENTID IN (SELECT c.contentid
  FROM CONTENT c
  JOIN BODYCONTENT bc
    ON c.contentid = bc.contentid
  JOIN SPACES s
    ON c.spaceid = s.spaceid
  WHERE c.content_status = 'draft'
    AND c.contenttype IN ('PAGE', 'BLOGPOST')
    AND bc.body LIKE '%ac:name="LaTeX block"%'
)
   AND propertyname = 'sync-rev-source'
;

update CONTENTPROPERTIES
set stringval = 'synchrony-recovery'
where CONTENTID IN (SELECT c.contentid
  FROM CONTENT c
  JOIN BODYCONTENT bc
    ON c.contentid = bc.contentid
  JOIN SPACES s
    ON c.spaceid = s.spaceid
  WHERE c.content_status = 'draft'
    AND c.contenttype IN ('PAGE', 'BLOGPOST')
    AND bc.body LIKE '%ac:name="LaTeX inline"%'
)
   AND propertyname = 'sync-rev-source'
;

UPDATE bodycontent
SET body = replace(body,'ac:name="LaTeX block"','ac:name="latex-block"')
WHERE bodycontentid in (
  SELECT bc.bodycontentid
  FROM CONTENT c
  JOIN BODYCONTENT bc
      ON c.contentid = bc.contentid
  WHERE c.contenttype IN ('PAGE', 'BLOGPOST', 'COMMENT')
    AND bc.body LIKE '%ac:name="LaTeX block"%'
)
;

UPDATE bodycontent
SET body = replace(body,'ac:name="LaTeX inline"','ac:name="latex-inline"')
WHERE bodycontentid in (
  SELECT bc.bodycontentid
  FROM CONTENT c
  JOIN BODYCONTENT bc
      ON c.contentid = bc.contentid
  WHERE c.contenttype IN ('PAGE', 'BLOGPOST', 'COMMENT')
    AND bc.body LIKE '%ac:name="LaTeX inline"%'
)
;

UPDATE bodycontent
SET body = replace(body,'ac:name="LaTeX block"','ac:name="latex-block"')
WHERE bodycontentid in (
  SELECT bc.bodycontentid
  FROM CONTENT c
  JOIN BODYCONTENT bc
      ON c.contentid = bc.contentid
  WHERE c.content_status = 'draft'
    AND c.contenttype IN ('PAGE', 'BLOGPOST')
    AND bc.body LIKE '%ac:name="LaTeX block"%'
)
;

UPDATE bodycontent
SET body = replace(body,'ac:name="LaTeX inline"','ac:name="latex-inline"')
WHERE bodycontentid in (
  SELECT bc.bodycontentid
  FROM CONTENT c
  JOIN BODYCONTENT bc
      ON c.contentid = bc.contentid
  WHERE c.content_status = 'draft'
    AND c.contenttype IN ('PAGE', 'BLOGPOST')
    AND bc.body LIKE '%ac:name="LaTeX inline"%'
)
;
```

### Explanation of the above queries

#### Make Synchrony update its cache

**If Collaborative Editing is enabled**, change the properties of target shared drafts so that Synchrony updates its cache with the modified content.

**LaTeX block** macro

#### PostgreSQL

```sql
update CONTENTPROPERTIES
set stringval = 'synchrony-recovery'
where CONTENTID IN (SELECT c.contentid
  FROM CONTENT c
  JOIN BODYCONTENT bc
    ON c.contentid = bc.contentid
  JOIN SPACES s
    ON c.spaceid = s.spaceid
  WHERE c.content_status = 'draft'
    AND c.contenttype IN ('PAGE', 'BLOGPOST')
    AND bc.body LIKE '%ac:name="LaTeX block"%'
)
   AND propertyname = 'sync-rev-source'
;
```

**LaTeX inline** macro

#### PostgreSQL

```sql
update CONTENTPROPERTIES
set stringval = 'synchrony-recovery'
where CONTENTID IN (SELECT c.contentid
  FROM CONTENT c
  JOIN BODYCONTENT bc
    ON c.contentid = bc.contentid
  JOIN SPACES s
    ON c.spaceid = s.spaceid
  WHERE c.content_status = 'draft'
    AND c.contenttype IN ('PAGE', 'BLOGPOST')
    AND bc.body LIKE '%ac:name="LaTeX inline"%'
)
   AND propertyname = 'sync-rev-source'
;
```

#### Update the content of Pages, Blog posts, and Page Comments

Run the following SQL query to update the content of Pages, Blog posts, and Page Comments.

**LaTeX block** macro

#### PostgreSQL

```sql
UPDATE bodycontent
SET body = replace(body,'ac:name="LaTeX block"','ac:name="latex-block"')
WHERE bodycontentid in (
  SELECT bc.bodycontentid
  FROM CONTENT c
  JOIN BODYCONTENT bc
      ON c.contentid = bc.contentid
  WHERE c.contenttype IN ('PAGE', 'BLOGPOST', 'COMMENT')
    AND bc.body LIKE '%ac:name="LaTeX block"%'
)
;
```

**LaTeX inline** macro

#### PostgreSQL

```sql
UPDATE bodycontent
SET body = replace(body,'ac:name="LaTeX inline"','ac:name="latex-inline"')
WHERE bodycontentid in (
  SELECT bc.bodycontentid
  FROM CONTENT c
  JOIN BODYCONTENT bc
      ON c.contentid = bc.contentid
  WHERE c.contenttype IN ('PAGE', 'BLOGPOST', 'COMMENT')
    AND bc.body LIKE '%ac:name="LaTeX inline"%'
)
;
```

#### **Update shared drafts**

**If Collaborative Editing is enabled**, update the body of shared drafts.

**LaTeX block** macro

#### PostgreSQL

```sql
UPDATE bodycontent
SET body = replace(body,'ac:name="LaTeX block"','ac:name="latex-block"')
WHERE bodycontentid in (
  SELECT bc.bodycontentid
  FROM CONTENT c
  JOIN BODYCONTENT bc
      ON c.contentid = bc.contentid
  WHERE c.content_status = 'draft'
    AND c.contenttype IN ('PAGE', 'BLOGPOST')
    AND bc.body LIKE '%ac:name="LaTeX block"%'
)
;
```

**LaTeX inline** macro

#### PostgreSQL

```sql
UPDATE bodycontent
SET body = replace(body,'ac:name="LaTeX inline"','ac:name="latex-inline"')
WHERE bodycontentid in (
  SELECT bc.bodycontentid
  FROM CONTENT c
  JOIN BODYCONTENT bc
      ON c.contentid = bc.contentid
  WHERE c.content_status = 'draft'
    AND c.contenttype IN ('PAGE', 'BLOGPOST')
    AND bc.body LIKE '%ac:name="LaTeX inline"%'
)
;
```

## **Start the Synchrony process**

**If Collaborative Editing is enabled** and Synchrony is running on a [standalone cluster](https://confluence.atlassian.com/doc/set-up-a-synchrony-cluster-for-confluence-data-center-958779073.html), start the Synchrony process on each node following your standard procedure.

## Start Confluence

Start Confluence following your standard procedure. If running Confluence Data Center, start Confluence on each node at a time.
