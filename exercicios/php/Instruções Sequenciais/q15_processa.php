<?php
	$raio = $_POST['raio'];
	
	print 'Perimetro:' . (2 * pi() * $raio); 
	print '<br>';
	print 'Área:' . (pi() * $raio * $raio);
?>