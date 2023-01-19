describe('CONSULTA VENDEDORES + LINEAS', () => {
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
          cy.get('#ven_btn').click()
          cy.get('#vendedores > :nth-child(1) > .form-check-input').click()
          cy.get('#vendedores > :nth-child(4) > .form-check-input').click()
          cy.get('#ven_btn').click()
          cy.get('#client_btn').click()
          cy.get('#grupo4client').click() 
          cy.get('#grupo4clientes > :nth-child(3) > .form-check-input').click()
          cy.get('#button-addon1').click()
        
  
      });
  });