<?php
	$a = $_POST['a'];
	$b = $_POST['b'];
	$c = $_POST['c'];

	$delta = $b*$b - 4 *$a * $c;

	$x1 = (-$b + sqrt($delta))/ (2 * $a);
	$x2 = (-$b - sqrt($delta))/ (2 * $a);

	print 'As raizes são ' . $x1 .' e '. $x2; 
?>