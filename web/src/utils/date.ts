export function iso2date(iso: Date) {
  return new Date(iso).toLocaleDateString();
}
