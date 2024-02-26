import { QueryClient, QueryClientProvider } from "@tanstack/react-query";
import VisitsBoard from "./components/VisitsBoard";
import CreateVisit from "./components/CreateVisit";

const queryClient = new QueryClient();

export default function App() {
  return (
    <QueryClientProvider client={queryClient}>
      <div className="h-screen w-full overflow-auto p-12 bg-white dark:bg-neutral-900 text-slate-900 dark:text-neutral-50">
        <div className="flex flex-wrap items-center justify-between sm:flex-nowrap mb-8">
          <h1 className="text-xl font-semibold leading-6">Houm visits manager</h1>
          <div className="flex-shrink-0">
            <CreateVisit />
          </div>
        </div>
        <VisitsBoard />
      </div>
    </QueryClientProvider>
  );
}
