import icons from './product-icons.json';

/** Specific platform prefixes take priority over the shared product identity. */
export function productIcon(path: string): string | undefined {
  const slug = path.replace(/^\/+|\/+$/g, '') + '/';
  const match = icons.find(({ prefix }) => slug.startsWith(prefix));
  return match ? import.meta.env.BASE_URL.replace(/\/?$/, '/') + match.icon : undefined;
}
