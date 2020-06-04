<?php
$months = array(
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
);

$im = (int)readline() - 1;
if($im < 12)
    echo $months[$im];
else
    echo "Invalid Month!";