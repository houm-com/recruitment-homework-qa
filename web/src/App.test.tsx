import { expect, test } from "vitest";
import { render, screen } from "@testing-library/react";
import App from "./App";

test("App should render", () => {
  render(<App />);
  expect(screen.getByText("hello world")).toBeInTheDocument();
});
