import { z } from "zod";
import { visitStatusSchema } from "./VisitStatus";

export const visitSchema = z.object({
  id: z.number(),
  address: z.string(),
  houmer_name: z.string().nullable(),
  visitor_name: z.string().nullable(),
  scheduled_at: z.string(),
  status: visitStatusSchema,
  resolution_comment: z.string().nullable(),
  created_at: z.string(),
  updated_at: z.string(),
});

export type Visit = z.infer<typeof visitSchema>;
