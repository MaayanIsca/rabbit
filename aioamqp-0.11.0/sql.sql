select  ar.name artistName, g.name genreName
from tracks t 
join albums a on a.AlbumId=t.AlbumId
join artists ar on ar.artistId= a.artistId
join genres g on g.genreId=t.genreId;
select c.FirstName||' '||c.LastName as name, c.Phone, c.Email,c.Address||' '||c.City||' '||c.Country as address, count(ii.trackId) countOfDisks
from customers c
join invoices i on i.customerId= c.customerId
join invoice_items ii on ii.invoiceId=i.invoiceId
group by c.FirstName||' '||c.LastName, c.Phone, c.Email,c.Address||' '||c.City||' '||c.Country;
select count(substr(cus.Email, instr(cus.email, '@') + 1)) as num_domain,cus.country 
from customers cus 
group by cus.country;
select count(ii.trackId) sum,i.billingCountry AS Country  
from invoices i 
join invoice_items ii on i.invoiceId=ii.invoiceId 
group by i.billingCountry;
select max(a.count) countMax,a.trackId,a.country from (
select count(ii.trackId) count,ii.trackId,i.billingCountry AS Country 
from invoices i 
join invoice_items ii on i.invoiceId=ii.invoiceId 
group by ii.tracKId, i.billingCountry) a
group by a.trackId, a.country;
select b.CustomerId, b.name from(
select a.CustomerId, a.name, a.a+a.b+a.c+a.d+a.e+a.f+a.g+a.h+a.i as count from(
SELECT c.CustomerId,  c.FirstName||' '||c.LastName as name, CASE WHEN c.Phone IS NULL THEN 1 ELSE 0 END a,
CASE WHEN c.Email IS NULL THEN 1 ELSE 0 END b,
CASE WHEN c.address IS NULL THEN 1 ELSE 0 END c,
CASE WHEN c.fax IS NULL THEN 1 ELSE 0 END d,
CASE WHEN c.postalCode IS NULL THEN 1 ELSE 0 END e,
CASE WHEN c.company IS NULL THEN 1 ELSE 0 END f,
CASE WHEN c.state IS NULL THEN 1 ELSE 0 END g,
CASE WHEN c.city IS NULL THEN 1 ELSE 0 END h,
CASE WHEN c.country IS NULL THEN 1 ELSE 0 END i
FROM customers c) a)b  where b.count>1;
