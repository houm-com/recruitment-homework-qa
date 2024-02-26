import { api } from "@/utils/api";
import { useQuery } from "@tanstack/react-query";
import { z } from "zod";
import { visitStatusSchema } from "@/types/VisitStatus";

const getVisitsStatusResponseSchema = z.array(visitStatusSchema);

export function useGetVisitsStatus() {
  return useQuery({
    queryKey: ["visits-status"],
    queryFn: async () => {
      const response = await api.get("/visits/status/options");
      return getVisitsStatusResponseSchema.parse(response);
    },
  });
}
