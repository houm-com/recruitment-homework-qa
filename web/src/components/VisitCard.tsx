import { Visit } from "@/types/Visit";
import { iso2date } from "@/utils/date";

function isDelayed(scheduledAt: string) {
  return new Date(scheduledAt) < new Date();
}

export default function VisitCard({ visit }: { visit: Visit }) {
  return (
    <div className="cursor-pointer rounded border bg-neutral-200 dark:bg-neutral-800/50 border-neutral-700 p-3">
      <h4 className="text-xl mb-1">{visit.address}</h4>
      <p className="text-sm mb-2">
        {iso2date(visit.scheduled_at)}{" "}
        {isDelayed(visit.scheduled_at) && (
          <span className="italic text-red-700 dark:text-red-300">(Delayed)</span>
        )}
      </p>
      <p>Visitor: {visit.visitor_name}</p>
      <p>
        Houmer:{" "}
        {visit.houmer_name ? (
          visit.houmer_name
        ) : (
          <span className="italic text-red-700 dark:text-red-300">unassigned</span>
        )}
      </p>
      {(visit.status === "COMPLETED" || visit.status === "CANCELED") && (
        <>
          <p className="mt-4">Resolution</p>
          <p className="italic">{visit.resolution_comment}</p>
        </>
      )}
    </div>
  );
}
