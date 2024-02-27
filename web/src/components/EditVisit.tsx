import { useState } from "react";
import { useForm } from "react-hook-form";
import { z } from "zod";
import { zodResolver } from "@hookform/resolvers/zod";
import Button from "@/ui/Button";
import { Modal, ModalTitle, ModalBody, ModalActions } from "@/ui/Modal";
import Input from "@/ui/Input";
import { Visit } from "@/types/Visit";
import { visitStatusSchema } from "@/types/VisitStatus";
import { useEditVisit } from "@/actions/edit-visit";
import Select from "@/ui/Select";

const editSchema = z
  .object({
    address: z.string({ required_error: "Address is required" }).min(1),
    visitor_name: z.string({ required_error: "Visitor name is required" }).min(1),
    houmer_name: z.string().nullable(),
    scheduled_at: z.coerce.date({ required_error: "Scheduled time is required" }),
    status: visitStatusSchema,
    resolution_comment: z.string().nullable(),
  })
  .refine(
    (data) => {
      if (data.status === "COMPLETED" || data.status === "CANCELED") {
        return data.resolution_comment !== undefined;
      }
      return true;
    },
    {
      message: "Resolution comment is required for completed or canceled visits",
      path: ["resolution_comment"],
    },
  );

type CreateVisitForm = z.infer<typeof editSchema>;
export default function EditVisit({ visit }: { visit: Visit }) {
  const [open, setOpen] = useState(false);
  const {
    register,
    handleSubmit,
    reset,
    formState: { errors },
    watch,
  } = useForm<CreateVisitForm>({
    values: {
      ...visit,
      scheduled_at: new Date(visit.scheduled_at).toISOString().slice(0, 16) as unknown as Date,
    },
    reValidateMode: "onSubmit",
    resolver: zodResolver(editSchema),
  });

  const showComment = watch("status") === "COMPLETED" || watch("status") === "CANCELED";
  const { mutate, status: submitStatus, error: submitError } = useEditVisit({ id: visit.id });
  const handleClose = () => {
    if (submitStatus === "pending") {
      return;
    }
    reset();
    setOpen(false);
  };
  const onSubmit = (data: CreateVisitForm) => {
    mutate(data, {
      onSuccess: () => {
        handleClose();
      },
    });
  };
  return (
    <>
      <Button onClick={() => setOpen(true)} size="sm" variant="secondary">
        Edit
      </Button>
      <Modal open={open} onClose={handleClose}>
        <ModalTitle>Edit visit ({visit.id})</ModalTitle>
        <ModalBody>
          {submitStatus === "error" && (
            <div className="text-red-600 my-6">{submitError?.message}</div>
          )}
          <form className="flex flex-col gap-3" onSubmit={handleSubmit((data) => onSubmit(data))}>
            <Input
              label="Address"
              {...register("address")}
              disabled={submitStatus === "pending"}
              error={errors.address?.message && `${errors.address.message}`}
            />
            <Input
              label="Visitor name"
              {...register("visitor_name")}
              disabled={submitStatus === "pending"}
              error={errors.visitor_name?.message && `${errors.visitor_name.message}`}
            />
            <Input label="Houmer name" {...register("houmer_name")} />
            <Input
              label="Scheduled time"
              {...register("scheduled_at")}
              type="datetime-local"
              disabled={submitStatus === "pending"}
              error={errors.scheduled_at?.message && `${errors.scheduled_at.message}`}
            />
            <Select
              label="Status"
              {...register("status")}
              disabled={submitStatus === "pending"}
              error={errors.status?.message && `${errors.status.message}`}
              options={[
                { label: "Pending", value: "PENDING" },
                { label: "Delayed", value: "DELAYED" },
                { label: "In progress", value: "IN_PROGRESS" },
                { label: "Completed", value: "COMPLETED" },
                { label: "Canceled", value: "CANCELED" },
              ]}
            />
            {showComment && (
              <Input
                label="Resolution comment"
                {...register("resolution_comment")}
                disabled={submitStatus === "pending"}
                error={errors.resolution_comment?.message && `${errors.resolution_comment.message}`}
              />
            )}
            <ModalActions>
              <Button variant="secondary" onClick={handleClose}>
                Cancel
              </Button>
              <Button type="submit">Edit</Button>
            </ModalActions>
          </form>
        </ModalBody>
      </Modal>
    </>
  );
}
