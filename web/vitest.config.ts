/// <reference types="vite/client" />
/// <reference types="vitest" />

import { defineConfig, mergeConfig } from "vitest/config";
import viteConfig from "./vite.config.ts";

export default mergeConfig(
  viteConfig,
  defineConfig({
    test: {
      globals: true,
      environment: "jsdom",
      setupFiles: "./src/utils/test/vitest.setup.ts",
    },
  }),
);
