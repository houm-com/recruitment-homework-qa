import z from "zod";

export const visitStatusSchema = z.enum([
  "PENDING",
  "DELAY",
  "IN_PROGRESS",
  "COMPLETED",
  "CANCELED",
]);

export type VisitStatus = z.infer<typeof visitStatusSchema>;
