select 
select c.FirstName||' '||c.LastName as name, c.Phone, c.Email,c.Address||' '||c.City||' '||c.Country as adress from customers c
select count(substr(cus.Email, instr(cus.email, '@') + 1)) as num_domain,cus.country from customers cus group by cus.country
select count(ii.trackId) sum,i.billingCountry AS Country  from invoices i join invoice_items ii on i.invoiceId=ii.invoiceId group by i.billingCountry
select count(ii.trackId) count,ii.trackid,i.billingCountry AS Country  from invoices i join invoice_items ii on i.invoiceId=ii.invoiceId group by ii.trackid, i.billingCountry

select c.FirstName||' '||c.LastName as name from customers c join 

select * from invoices i join invoice_items ii on i.invoiceId=ii.invoiceId 
