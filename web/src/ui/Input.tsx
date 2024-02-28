import { forwardRef } from "react";
import { VariantProps, cva } from "class-variance-authority";

const input = cva(
  [
    "block w-full rounded-md border-0 p-1.5  shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6",
    "bg-neutral-200 dark:bg-neutral-800",
    "text-gray-900 dark:text-neutral-50",
    "disabled:bg-slate-50 disabled:text-slate-300 dark:disabled:bg-gray-800 disabled:cursor-not-allowed",
  ],
  {
    variants: {},
    defaultVariants: {},
  },
);

export interface InputProps
  extends React.InputHTMLAttributes<HTMLInputElement>,
    VariantProps<typeof input> {
  label: string;
  error?: string;
}

export default forwardRef(function Input(
  { error, label, id, ...props }: InputProps,
  ref: React.Ref<HTMLInputElement>,
) {
  return (
    <div>
      <label htmlFor={id} className="block text-sm font-medium leading-6">
        {label}
      </label>
      <div className="mt-2">
        <input id={id} ref={ref} className={input({})} {...props} />
      </div>
      {error && <p className="mt-2 text-sm text-red-600">{error}</p>}
    </div>
  );
});
