describe('CONSULTA VENDEDORES', () => {
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
          cy.get('#item_btn').click()
          cy.get('#grupo1').click()
          cy.get('#grupo1Vendedores > :nth-child(2) > .form-check-input').click()
          cy.get('#grupo1Vendedores > :nth-child(4) > .form-check-input').click()
          cy.get('#grupo1Vendedores > :nth-child(8) > .form-check-input').click()
          cy.get('#button-addon1').click()
  
      });
  });