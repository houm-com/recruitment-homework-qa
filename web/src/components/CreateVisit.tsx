import { useState } from "react";
import Button from "@/ui/Button";
import { Modal, ModalTitle, ModalBody, ModalActions } from "@/ui/Modal";

export default function CreateVisit() {
  const [open, setOpen] = useState(false);
  const onClose = () => setOpen(false);
  return (
    <>
      <Button onClick={() => setOpen(true)}>Create visit</Button>
      <Modal open={open} onClose={onClose}>
        <ModalTitle>Create a visit</ModalTitle>
        <ModalBody>
          <p>Content goes here</p>
          <ModalActions>
            <Button variant="secondary" onClick={onClose}>
              Cancel
            </Button>
            <Button onClick={onClose}>Create</Button>
          </ModalActions>
        </ModalBody>
      </Modal>
    </>
  );
}
