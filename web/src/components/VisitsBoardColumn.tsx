import { Visit } from "@/types/Visit";
import VisitCard from "./VisitCard";

export default function VisitsBoardColumn({ title, visits }: { title: string; visits: Visit[] }) {
  return (
    <div className="w-56 shrink-0">
      <div className="mb-3 flex items-center justify-between">
        <h3 className="font-medium">{title}</h3>
        <span className="rounded text-sm text-neutral-700 dark:text-neutral-400">
          {visits.length}
        </span>
      </div>
      <div className="h-full w-full flex flex-col gap-2">
        {visits.map((visit) => (
          <VisitCard key={visit.id} visit={visit} />
        ))}
      </div>
    </div>
  );
}
