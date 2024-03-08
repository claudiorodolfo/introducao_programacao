<?php
	$numero1 = $_POST['numero1'];
	$numero2 = $_POST['numero2'];
	$numero3 = $_POST['numero3'];
	
	if ($numero1 <= $numero2 && $numero2 <= $numero3)
		print 'Os números estão crescentes!';
	else if ($numero1 >= $numero2 && $numero2 >= $numero3)
		print 'Os números estão decrescentes!';
	else
		print 'Os números estão fora de ordem!';

?>