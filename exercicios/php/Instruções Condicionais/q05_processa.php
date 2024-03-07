<?php
	$valor = $_POST['valor'];
	
	if ($valor % 4 == 0) {
		if ($valor % 100 != 0) {
			print 'Não é bissexto';
		} else {
			if ($valor % 400 == 0) {
				print 'É bissexto';
			} else {
				print 'Não é bissexto';
			}
		}
	} else {
		print 'Não é bissexto';
	}
?>