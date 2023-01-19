describe('CONSULTA FECHA GENERAL', () => {
  let data; 
  before(() => {
    cy.fixture('example').then((fData) => {
        data = fData;
    });
  });

    it('Usuario es correcto', () => {
        Cypress.config('pageLoadTimeout')
        cy.visit('/')
        cy.get('.btn').click()
        cy.get('#username').type(data.user)
        cy.get('#password')
        cy.get('.btn').click()
        cy.get('.flex-md-nowrap > .btn-primary').click()
        cy.get('#datepicker > .form-control').click().type(data.date)
        cy.get('#exampleModal').click()
        cy.get('#button-addon1').click()

    });
});