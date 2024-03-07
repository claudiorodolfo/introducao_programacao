<?php
	$anguloGrau = $_POST['angulo'];
	$anguloRadiano = ($anguloGrau * pi())/180;
	$seno = sin($anguloRadiano);
	$cosseno = cos($anguloRadiano);
	print 'Seno: ' . $seno . ', Cosseno: ' . $cosseno;
?>