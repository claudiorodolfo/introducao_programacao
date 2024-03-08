<?php
	$peso = $_POST['peso'];
	$frete = $_POST['frete'];

	if($peso > 10)
		print 'Frete:'. $frete * 1.2;
	else
		print 'Frete:'. $frete;

?>