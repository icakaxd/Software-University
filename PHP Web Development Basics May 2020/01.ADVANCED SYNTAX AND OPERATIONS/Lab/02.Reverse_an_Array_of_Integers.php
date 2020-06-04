<?php
$n = (int)readline();
$arr = Array();
$result = '';

for($i = 0; $i < $n; $i++)
    $arr[] = (int)readline();

foreach (array_reverse($arr) as $item){
    if(!strlen($result))
        $result = $item;
    else
        $result .= " $item";
}

echo $result;