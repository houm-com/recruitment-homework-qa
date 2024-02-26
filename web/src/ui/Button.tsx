import { forwardRef } from "react";

export default forwardRef(function Button(
  { children, ...props }: React.ButtonHTMLAttributes<HTMLButtonElement>,
  ref: React.Ref<HTMLButtonElement>,
) {
  return (
    <button
      ref={ref}
      className="inline-flex items-center rounded-md bg-indigo-600 px-3 py-2 text-sm font-semibold text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-500"
      {...props}
    >
      {children}
    </button>
  );
});
