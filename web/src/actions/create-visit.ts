import { api } from "@/utils/api";
import { useMutation, useQueryClient } from "@tanstack/react-query";

export function useCreateVisit<T>() {
  const queryClient = useQueryClient();
  return useMutation({
    mutationFn: (visit: T) => api.post<T>("/visits", visit),
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ["visits"] });
    },
  });
}
