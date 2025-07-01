00010444 <compute_passcode>:
   10444:	7179                	addi	sp,sp,-48 // allocate space for stack pointer
   10446:	d606                	sw	ra,44(sp) // ra
   10448:	d422                	sw	s0,40(sp) // s0
   1044a:	1800                	addi s0, sp ,48 // s0 = sp + 48 -> s0 = 
   1044c:	fca42e23          	    sw	a0,-36(s0) // -36 = input
   10450:	fe042623          	    sw	zero,-20(s0) // -20 = 0
   10454:	a825                	j	1048c <compute_passcode+0x48> // j to the function
   10456:	fec42783          	    lw	a5,-20(s0)
   1045a:	0795                	addi	a5,a5,5
   1045c:	fdc42703          	    lw	a4,-36(s0)
   10460:	00f757b3          	    srl	a5,a4,a5
   10464:	fdc42703          	    lw	a4,-36(s0)
   10468:	8fb9                	xor	a5,a5,a4
   1046a:	fcf42e23          	    sw	a5,-36(s0)
   1046e:	fdc42703          	    lw	a4,-36(s0)
   10472:	27d4f7b7          	    lui	a5,0x27d4f
   10476:	b2d78793          	    addi	a5,a5,-1235 # 27d4eb2d <__global_pointer$+0x27d3c31d>
   1047a:	02f707b3          	    mul	a5,a4,a5
   1047e:	fcf42e23          	    sw	a5,-36(s0)
   10482:	fec42783          	    lw	a5,-20(s0)
   10486:	0785                	addi	a5,a5,1
   10488:	fef42623          	    sw	a5,-20(s0)
   1048c:	fec42703          	    lw	a4,-20(s0) / a4 = 0
   10490:	4789                	li	a5,2
   10492:	fce7d2e3          	    bge	a5,a4,10456 <compute_passcode+0x12>
   10496:	fdc42783          	    lw	a5,-36(s0)
   1049a:	853e                	mv	a0,a5
   1049c:	50b2                	lw	ra,44(sp)
   1049e:	5422                	lw	s0,40(sp)
   104a0:	6145                	addi	sp,sp,48
   104a2:	8082                	ret
