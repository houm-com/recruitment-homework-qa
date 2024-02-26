import { forwardRef } from "react";
import { VariantProps, cva } from "class-variance-authority";

const button = cva(
  ["inline-flex w-full gap-2 justify-center border rounded font-semibold shadow-sm"],
  {
    variants: {
      variant: {
        primary: ["bg-red-600", "text-white", "hover:bg-red-500", "border-red-800"],
        secondary: ["border-red-800", "hover:bg-neutral-800"],
      },
      size: {
        sm: ["text-sm", "py-1", "px-2"],
        md: ["text-sm", "py-2", "px-3"],
      },
    },
    defaultVariants: {
      variant: "primary",
      size: "md",
    },
  },
);

export interface ButtonProps
  extends React.ButtonHTMLAttributes<HTMLButtonElement>,
    VariantProps<typeof button> {}

export default forwardRef(function Button(
  { children, variant, size, ...props }: ButtonProps,
  ref: React.Ref<HTMLButtonElement>,
) {
  return (
    <button ref={ref} className={button({ variant, size })} {...props}>
      {children}
    </button>
  );
});
