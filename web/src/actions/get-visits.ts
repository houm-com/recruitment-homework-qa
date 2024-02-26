import { api } from "@/utils/api";
import { useQuery } from "@tanstack/react-query";
import { z } from "zod";
import { visitSchema } from "@/types/Visit";

const getVisitsResponse = z.array(visitSchema);

export function useGetVisits() {
  return useQuery({
    queryKey: ["visits"],
    queryFn: async () => {
      const response = await api.get("/visits");
      return getVisitsResponse.parse(response);
    },
  });
}
