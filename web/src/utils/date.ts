export function iso2date(iso: string) {
  return new Date(iso).toLocaleDateString();
}
