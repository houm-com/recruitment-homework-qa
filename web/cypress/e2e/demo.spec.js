describe("login", () => {
  it("user should be able to log in", () => {
    cy.visit("/");
    cy.contains("hello world").should("be.visible");
  });
});
