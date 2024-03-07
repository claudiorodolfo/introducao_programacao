<?php
	$valor1 = $_POST['valor1'];
	$valor2 = $_POST['valor2'];
	$valor3 = $_POST['valor3'];
	$media = ($valor1*4 + $valor2*7 + $valor3*3)/14;
	print 'A média ponderada é ' . $media;
?>