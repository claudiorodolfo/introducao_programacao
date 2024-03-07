<?php
	$valor = $_POST['valor'];

	if($valor > 100)
		print 'Preço Final:'. $valor * 0.95;
	else
		print 'Preço Final:'. $valor;

?>