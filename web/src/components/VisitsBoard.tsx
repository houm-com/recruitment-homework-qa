import { useGetVisits } from "@/actions/get-visits";
import { useGetVisitsStatus } from "@/actions/get-visits-status";
import VisitsBoardColumn from "./VisitsBoardColumn";

export default function VisitsBoard() {
  const visitStatus = useGetVisitsStatus();
  const visits = useGetVisits();
  if (visitStatus.status === "pending") return <div>Loading...</div>;
  if (visitStatus.status === "error") return <div>{visitStatus.error.message}</div>;
  return (
    <div className="flex h-full w-full gap-3 overflow-auto p-12">
      {visitStatus.data.map((status) => (
        <VisitsBoardColumn
          key={status}
          title={status}
          visits={
            visits.status === "success"
              ? visits.data.filter((visit) => visit.status === status)
              : []
          }
        />
      ))}
    </div>
  );
}
