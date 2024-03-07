<?php
	$valor = $_POST['valor'];
	
	if ($valor > 0) {
		print 'Positivo';
	} else {
		if ($valor == 0) {
			print 'Neutro';
		} else {
			print 'Negativo';
		}
	}
?>