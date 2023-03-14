select count(Survived) as num_of_survivors,
CASE
when Age >= 60 then "elderlies"
when Age < 18 then "children"
when Age >= 18 and Age < 60 then "adults"
end as passengers_survived_classification
from passengers
where Survived = 1
group by passengers_survived_classification
