import { useState } from "react";
import { useForm } from "react-hook-form";
import { z } from "zod";
import { zodResolver } from "@hookform/resolvers/zod";
import Button from "@/ui/Button";
import { Modal, ModalTitle, ModalBody, ModalActions } from "@/ui/Modal";
import Input from "@/ui/Input";
import { useCreateVisit } from "@/actions/create-visit";

const createSchema = z.object({
  address: z.string({ required_error: "Address is required" }).min(1),
  visitor_name: z.string({ required_error: "Visitor name is required" }).min(1),
  houmer_name: z.string().nullable(),
  scheduled_at: z.coerce.date({ required_error: "Scheduled time is required" }),
});

type CreateVisitForm = z.infer<typeof createSchema>;

export default function CreateVisit() {
  const [open, setOpen] = useState(false);
  const {
    register,
    handleSubmit,
    reset,
    formState: { errors },
  } = useForm<CreateVisitForm>({
    reValidateMode: "onSubmit",
    resolver: zodResolver(createSchema),
  });
  const { mutate, status: submitStatus, error: submitError } = useCreateVisit();
  const handleClose = () => {
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
      <Button onClick={() => setOpen(true)}>Create visit</Button>
      <Modal open={open} onClose={handleClose}>
        <ModalTitle>Create a visit</ModalTitle>
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
            <ModalActions>
              <Button variant="secondary" onClick={handleClose}>
                Cancel
              </Button>
              <Button type="submit">Create</Button>
            </ModalActions>
          </form>
        </ModalBody>
      </Modal>
    </>
  );
}
