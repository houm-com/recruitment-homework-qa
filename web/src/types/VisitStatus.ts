import z from "zod";

export const visitStatusSchema = z.enum([
  "PENDING",
  "DELAYED",
  "IN_PROGRESS",
  "CANCELED",
  "COMPLETED",
]);

export type VisitStatus = z.infer<typeof visitStatusSchema>;
