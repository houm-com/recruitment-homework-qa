import React from "react";
import { render } from "@testing-library/react";
import { QueryClient, QueryClientProvider } from "@tanstack/react-query";

const queryClient = new QueryClient();

// eslint-disable-next-line react-refresh/only-export-components
const AllTheProviders = ({ children }: { children: React.ReactElement }) => {
  return <QueryClientProvider client={queryClient}>{children}</QueryClientProvider>;
};

// eslint-disable-next-line @typescript-eslint/ban-ts-comment
//@ts-ignore
const customRender = (ui, options) => render(ui, { wrapper: AllTheProviders, ...options });

// eslint-disable-next-line react-refresh/only-export-components
export * from "@testing-library/react";

// override render method
export { customRender as render };
