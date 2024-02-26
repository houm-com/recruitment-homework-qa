import { QueryClient, QueryClientProvider } from "@tanstack/react-query";
import VisitsBoard from "./components/VisitsBoard";

const queryClient = new QueryClient();

export default function App() {
  return (
    <QueryClientProvider client={queryClient}>
      <div className="h-screen w-full bg-white dark:bg-neutral-900 text-slate-900 dark:text-neutral-50">
        <VisitsBoard />
      </div>
    </QueryClientProvider>
  );
}
