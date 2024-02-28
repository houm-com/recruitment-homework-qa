import { forwardRef } from "react";
import { VariantProps, cva } from "class-variance-authority";

const select = cva(
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

export interface SelectProps
  extends React.SelectHTMLAttributes<HTMLSelectElement>,
    VariantProps<typeof select> {
  label: string;
  error?: string;
  options: { value: string; label: string }[];
}

export default forwardRef(function Select(
  { error, label, id, options, ...props }: SelectProps,
  ref: React.Ref<HTMLSelectElement>,
) {
  return (
    <div>
      <label htmlFor={id} className="block text-sm font-medium leading-6">
        {label}
      </label>
      <div className="mt-2">
        <select id={id} ref={ref} className={select({})} {...props}>
          {options.map((option) => (
            <option key={option.value} value={option.value}>
              {option.label}
            </option>
          ))}
        </select>
      </div>
      {error && <p className="mt-2 text-sm text-red-600">{error}</p>}
    </div>
  );
});
