SELECT * 
from carspecs join rentlocation
where vehicletype like 'suv';

---

select * 
from carspecs join rentlocation
where rating > 4.69 ;

---

select * 
from carspecs join rentlocation
where ratedaily < 100;

---

select ownerid, rating, vehiclemodel, vehicletype, vehiclemake, vehicleyear
from carspecs 
where ownerid = 641610;

---

select locationcity, locationstate, ownerid
from rentlocation
where locationcity like 'Portland' 
or locationcity like 'New Orleans'
or locationcity like 'Las Vegas';
