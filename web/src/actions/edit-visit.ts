import { api } from "@/utils/api";
import { useMutation, useQueryClient } from "@tanstack/react-query";

export function useEditVisit<T>({ id }: { id: number }) {
  const queryClient = useQueryClient();
  return useMutation({
    mutationFn: (visit: T) => api.patch<T>(`/visits/${id}`, visit),
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ["visits"] });
    },
  });
}
