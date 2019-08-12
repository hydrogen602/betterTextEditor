
#
# start moving everything into
# the class so that things
# can be packed a bit better
#


# f = open('debug.log', 'w')
# # f.write(str(colors))
# f.close()

specialInstructions = [
    'DB', 'DW', 'DD', 'DQ', 'DT', 'DO', 'DY', 'DZ', 
    'RESB', 'RESW', 'RESD', 'RESQ', 'REST', 'RESO', 
    'RESY', 'RESZ', 'INCBIN'
]

builtins = [
    'vdivpd', 'cvtss2si', 'vcmpgtpd', 'xsha1', 'scasw', 'vprotb', 'aad', 'vunpckhps', 
    'sha1rnds4', 'sbb', 'vmovntqq', 'crc32', 'vcmpneqsd', 'vfnmadd123sd', 'movdqa', 
    'unpcklpd', 'verw', 'blsfill', 'cmpneqss', 'ucomisd', 'vmovups', 'vfnmsub213ps', 
    'vcmptrue_usss', 'maxss', 'vpexpandb', 'vmaxpd', 'movd', 'vandps', 'vcmpordpd', 
    'stgi', 'vpcomw', 'psubsb', 'sysenter', 'vcmpgtps', 'vpopcntd', 'vfmadd123ss', 
    'phaddd', 'pextrw', 'pmovzxbw', 'vinsertf64x2', 'ficom', 'vcmpngt_uqsd', 'paddusb', 
    'vcomiss', 'vpexpandd', 'adc', 'paddsb', 'movsldup', 'vbroadcasti32x8', 
    'vcmpnge_ussd', 'vpavgw', 'hint_nop50', 'vcmpnle_uspd', 'vcmpngepd', 'vshufi64x2', 
    'vmxon', 'vcmpngtpd', 'pmovsxwq', 'fiadd', 'roundpd', 'b.1.25', 'vgatherpf1qps', 
    'insw', 'popad', 'vmovapd', 'vpcmpestri', 'vfmsubps', 'fucomip', 'fstenv', 'rdm', 
    'hint_nop22', 'vfmsub132sd', 'daa', 'phaddw', 'hint_nop49', 'vpmovsxbd', 'fyl2xp1', 
    'vfnmadd132sd', 'cmpxchg', 'hint_nop63', 'cmpunordpd', 'vcmptrue_uqps', 
    'vgf2p8mulb', 'pshuflw', 'vcmpneq_ossd', 'lwpval', 'pavgusb', 'vfmadd321sd', 
    'vcmpnlt_uqpd', 'vpmaxuw', 'vphaddbq', 'llwpcb', 'vminpd', 'vcvtusi2sd', 'vcmppd', 
    'xsave', 'vphsubd', 'ldmxcsr', 'vmaxss', 'vpmacssdd', 'pcmpgtq', 'vbroadcastf32x2', 
    'b.1.22', 'vcmpltss', 'ktestw', 'invlpg', 'psignd', 'fbstp', 'cmpss', 'vcvtsi2ss', 
    'rorx', 'blsic', 'fdisi', 'fcompp', 'vrsqrt14pd', 'vrangess', 'vpmaxsq', 'vgetexpps', 
    'hint_nop57', 'rdtsc', 'vcmpngt_uqps', 'sgdt', 'vfmsub312ss', 'vpbroadcastw', 
    'pmulhrwc', 'cvtps2pi', 'vminsd', 'vmovlhps', 'vcmpnless', 'vcmpneqps', 'hint_nop55', 
    'psrlw', 'pclmulhqhqdq', 'pmovsxdq', 'phsubw', 'v4dpwssd', 'pxor', 'vpmovq2m', 
    'outsw', 'vaesdec', 'hint_nop48', 'vpermq', 'sha256msg2', 'vpblendw', 'vphaddudq', 
    'kunpckdq', 'vcmpord_sss', 'v4fmaddps', 'ud0', 'hint_nop18', 'kortestd', 'fnstenv', 
    'vpermt2b', 'kandnb', 'vcmpps', 'vcmplt_ospd', 'pfrcpit1', 'aaa', 'psubd', 'korq', 
    'lodsb', 'hint_nop13', 'rdmsr', 'vcmpgt_oqsd', 'prefetchwt1', 'extractps', 'b.1.10', 
    'scasd', 'fld1', 'vfmsubadd231ps', 'vcmpnge_usps', 'kunpckbw', 'cvttps2dq', 'fpatan', 
    'vcmpngess', 'vucomiss', 'pfmin', 'svts', 'vmresume', 'vroundpd', 'vpmovsdw', 
    'vpmovdb', 'pextrb', 'b.1.32', 'vblendmpd', 'vpmacssww', 'cmpsq', 'vptestnmq', 
    'vblendvpd', 'cmpunordss', 'vpsubb', 'vmulss', 'cvttsd2si', 'vcvtsd2si', 'b.1.49', 
    'vpbroadcastd', 'b.1.5', 'blendps', 'vcvttpd2qq', 'smint', 'pfmax', 'pi2fw', 'fist', 
    'vgatherdpd', 'b.1.37', 'vfnmadd312pd', 'b.1.23', 'vcmpneq_osps', 'vfnmsub312pd', 
    'vcvttpd2uqq', 'vinsertps', 'vpslld', 'pi2fd', 'bndcn', 'stmxcsr', 'kxord', 
    'vcvttpd2udq', 'vroundss', 'movntss', 'pext', 'vfmsub321ps', 'b.1.3', 'cmpordps', 
    'bswap', 'loopnz', 'rcpss', 'vcmpnltss', 'vfnmadd312ps', 'pmaxsd', 'vscatterqpd', 
    'kmovw', 'vcvttsd2usi', 'mfence', 'vphaddwq', 'prefetcht2', 'sahf', 'knotw', 
    'vpandnq', 'vpacksswb', 'wrmsr', 'blcic', 'fistp', 'vcmpgtsd', 'kshiftrb', 'dmint',
    'fucom', 'scasb', 'subps', 'vpmovsxbq', 'pfcmpgt', 'vcmpnltsd', 'b.1.41', 'tpause', 
    'vxorpd', 'jcxz', 'vcmpngtss', 'vpcmpq', 'vcvtuqq2ps', 'pmvnzb', 'vrcp28pd', 'aam', 
    'vfmadd213ps', 'vbroadcasti64x4', 'cmpneqps', 'montmul', 'vcvtph2ps', 'vcmpeq_uspd', 
    'b.1.9', 'hint_nop46', 'xcryptofb', 'vgatherpf0qps', 'knotd', 'vpmacsdqh', 'fadd', 
    'vscatterpf1dpd', 'vpandq', 'vcmptrue_usps', 'vgatherpf1dpd', 'into', 'pfsubr', 
    'wbinvd', 'cmpunordps', 'fucompp', 'vandpd', 'vcmpngtsd', 'sqrtss', 'addps', 
    'vcmpord_ssd', 'vcmpeq_osps', 'hint_nop40', 'vpmovzxdq', 'pfrsqit1', 'vfpclassss', 
    'vpabsb', 'cvtps2pd', 'vpmaxub', 'vdivss', 'rsm', 'fldenv', 'haddpd', 'vmlaunch',
    'kaddq', 'cmpeqps', 'movaps', 'psubusb', 'b.1.20', 'vpunpcklbw', 'vcmpneq_osss', 
    'vcmpeq_ospd', 'vcmpge_osss', 'vpandn', 'iretw', 'vcvtss2si', 'xorps', 'fcomi', 
    'kaddb', 'fincstp', 'vshufpd', 'hint_nop56', 'hint_nop15', 'test', 'vpcomuq', 
    'vfnmadd321pd', 'vpshldq', 'fcom', 'vpinsrb', 'vcvtsi2sd', 'vfnmsub213sd', 'hint_nop37', 
    'int03', 'vfnmadd123ps', 'vcvtdq2pd', 'kshiftlw', 'vcmpngt_usps', 'vpunpckhqdq', 
    'fxrstor', 'loop', 'fst', 'vmovdqu32', 'pcmpestri', 'pminsb', 'subss', 'pcommit', 
    'vextractf128', 'fninit', 'vcvtpd2udq', 'vpshufd', 'vrndscalesd', 'hint_nop4', 'vpcomb', 
    'vpshlw', 'xsave64', 'vcmpfalse_oqps', 'paddb', 'vfmadd231ps', 'pmulhrsw', 'vpinsrw', 
    'vfmaddsub213ps', 'vfnmsubps', 'bndcu', 'vpsrldq', 'vcmpord_sps', 'aesdec', 'phsubsw', 
    'hint_nop14', 'cvtsi2sd', 'sfence', 'vcvtps2dq', 'vpmovm2d', 'cdqe', 'kxorb', 
    'pclmulhqlqdq', 'vrcp14sd', 'umwait', 'not', 'pswapd', 'pfacc', 'vpmovqw', 'vphminposuw', 
    'vaesenclast', 'divpd', 'kshiftrd', 'vfmsub321sd', 'vextractf64x2', 'vorps', 'vmulpd', 
    'vpmulhw', 'cmpneqsd', 'vpmacssdqh', 'ror', 'psubq', 'vpmovm2w', 'vrangesd', 'pextrd', 
    'vcmplt_oqss', 'vfmsub312sd', 'rcl', 'wrfsbase', 'pminud', 'xtest', 'vreducess', 'retnq', 
    'insb', 'vplzcntd', 'prefetch', 'tzmsk', 'vpshaw', 'pshufw', 'vfnmsub123pd', 'xsaveopt', 
    'vprotw', 'vfmadd213sd', 'paveb', 'vcvttss2usi', 'shlx', 'vpord', 'kandnq', 'packssdw', 
    'kandq', 'vfmaddsub231ps', 'vcmpngt_uqpd', 'vfmaddsub312ps', 'pmaddubsw', 'fsincos', 
    'movsx', 'vdbpsadbw', 'pushaw', 'vpexpandw', 'pmagw', 'vfmsubadd321ps', 'vpcompressq', 
    'vcmpnlt_uqsd', 'vfmadd312ps', 'rcr', 'pmovsxwd', 'b.1.42', 'por', 'pmvgezb', 'psrldq', 
    'bsf', 'vpmullw', 'vpmaddubsw', 'vpmovswb', 'vpmovzxbd', 'movq2dq', 'vaesdeclast', 
    'bndldx', 'fidiv', 'pminsw', 'vptestmq', 'hint_nop45', 'fabs', 'cmpxchg486', 'cvtpd2pi', 
    'rsqrtps', 'vmaskmovpd', 'hint_nop52', 'vpmovusdb', 'maxsd', 'cmpordpd', 'vcmpunord_spd', 
    'movdqu', 'xgetbv', 'maxps', 'vpshad', 'pushfq', 'vmovdqu', 'cvtpd2ps', 'vpmovzxbw', 
    'vpmaddwd', 'pminsd', 'vcmpordsd', 'vcmptrue_uspd', 'fyl2x', 'vcvttss2si', 'punpckhbw', 
    'vcmpneq_ospd', 'vpshld', 'kxnorb', 'vmaskmovps', 'sqrtsd', 'vpshrdd', 'vpmovsxwq', 
    'vldqqu', 'addpd', 'vblendvps', 'vcmpnltps', 'xcryptctr', 'vpextrw', 'paddw', 'rdtscp', 
    'vfmsubadd312ps', 'vpabsq', 'vfnmsub321ps', 'tzcnt', 'stosw', 'lgs', 'vpunpckhbw', 
    'vprolvd', 'b.1.53', 'b.1.21', 'vcmptruess', 'psignw', 'pmulhriw', 'vaddsubps', 'pavgw', 
    'kxnorq', 'cmpneqpd', 'vpextrb', 'vcvtusi2ss', 'vmovntdq', 'ret', 'vprorvd', 
    'vfnmadd312sd', 'pmovsxbw', 'vfmsub123sd', 'vmovntps', 'vporq', 'movntq', 'punpckldq', 
    'vtestps', 'vmovd', 'psllw', 'lgdt', 'bndcl', 'insertps', 'hint_nop31', 'loopz', 
    'vunpcklpd', 'pmvzb', 'vfmaddsub123ps', 'xrstor', 'vcmpneq_oqsd', 'sub', 'hint_nop59', 
    'bsr', 'rdfsbase', 'cwde', 'pextrq', 'vcmpngesd', 'vpminsw', 'pmaxsw', 'vpsrlq', 
    'kortestb', 'vpternlogq', 'salc', 'lfence', 'vscatterdpd', 'v4fnmaddps', 'vcmplt_oqps', 
    'hint_nop44', 'vcmpord_qss', 'ktestd', 'psubsiw', 'vcvttps2dq', 'vcmpnleps', 
    'vcmpeq_uqss', 'hint_nop12', 't1mskc', 'sal', 'movss', 'shld', 'cpu_read', 'loadall', 
    'pushad', 'vphaddubw', 'xlatb', 'vmulsd', 'vcmpgeps', 'vpshufbitqmb', 'pmovzxbd', 
    'vfnmsub132sd', 'aas', 'retw', 'vfnmsub132ss', 'fsave', 'cmpnleps', 'monitorx', 'kaddw', 
    'mul', 'xsavec64', 'vpmovusqd', 'vgf2p8affineqb', 'vpmaskmovd', 'xbts', 'vpermpd', 
    'fdivrp', 'mulss', 'vfmsub312ps', 'vblendpd', 'vcmpeq_usss', 'vprord', 'hint_nop21', 
    'retfw', 'vcmptrue_uqss', 'vfmadd312sd', 'fdivp', 'kxnord', 'ltr', 'vminss', 'hint_nop33', 
    'vfnmadd132ps', 'lsl', 'sysret', 'vfmsubsd', 'vfnmsub321pd', 'ffreep', 'hint_nop16', 'rol', 
    'cli', 'vpmaxuq', 'vcmpgt_osps', 'vcmpnge_usss', 'vcmple_oqss', 'vcmpless', 'insertq', 
    'vfmsub231pd', 'paddq', 'b.1.45', 'retf', 'pmaxub', 'vfmadd231ss', 'pmulld', 'vscalefss', 
    'vfmsubadd132pd', 'vcmpeqss', 'vfmaddsub213pd', 'vphaddbw', 'b.1.43', 'invvpid', 
    'hint_nop26', 'pfcmpeq', 'vcmplesd', 'vsqrtss', 'vpermi2q', 'vfnmsub123ps', 'psrlq', 
    'vpcmpestrm', 'vmaxps', 'vaeskeygenassist', 'vextractf64x4', 'fisub', 'hsubpd', 'vpaddusw', 
    'jecxz', 'vpcompressw', 'vfrczps', 'vinsertf128', 'vcmpnge_uqpd', 'vrsqrt14ps', 'fnop', 
    'vmovntpd', 'invpcid', 'vpmuludq', 'vpcmpeqd', 'vphaddw', 'vcmpunord_sps', 'cmpnlesd', 
    'fcomp', 'cmc', 'cvtsd2si', 'movups', 'lodsw', 'vcmplt_oqsd', 'vpgatherdd', 'vpackssdw', 
    'fsetpm', 'cmpsb', 'vpcomq', 'vfnmsub312ps', 'vrndscaleps', 'vcmpnlesd', 'vcvttsd2si', 
    'vptestmd', 'vfmadd132pd', 'vfmsubadd213pd', 'vfnmaddss', 'vpand', 'vptestmw', 'frstor', 
    'bts', 'hint_nop28', 'vcmpnle_usps', 'b.1.29', 'b.1.54', 'cpuid', 'vpermd', 'vbroadcastsd', 
    'fxch', 'vpandd', 'call', 'b.1.28', 'blsi', 'vaddps', 'vrsqrtps', 'pushfd', 'vcmple_osss', 
    'vreducesd', 'vinserti64x2', 'vfmsub132pd', 'vcmpgt_ospd', 'vpmovdw', 'vpmovsqw', 'fnsave', 
    'fcmovnbe', 'pinsrb', 'vaesenc', 'vfnmsub321ss', 'pf2iw', 'retn', 'shufpd', 'vcmplt_osps', 
    'vcmpordss', 'vpsraw', 'vextractf32x4', 'vrcpss', 'b.1.27', 'vrsqrtss', 'vfnmadd231ss', 
    'vcvtsd2ss', 'vcmpfalse_ospd', 'minpd', 'pmaddwd', 'stac', 'pfrcpit2', 'cld', 'fcomip', 
    'vpsravw', 'vfnmadd132pd', 'vcvtudq2ps', 'xcryptcbc', 'xstore', 'popfw', 'vcmpge_ossd', 
    'vfmaddsub231pd', 'clflushopt', 'vmovqqu', 'fcmovbe', 'svldt', 'hint_nop20', 'push', 'kmovq', 
    'vplzcntq', 'vpsubusw', 'vmaskmovdqu', 'vpaddq', 'maskmovq', 'smi', 'blendvpd', 'vcmple_ospd', 
    'vscalefsd', 'vfnmadd123ss', 'movapd', 'vpshufb', 'pclmullqlqdq', 'vorpd', 'sha1nexte', 'pushf',
    'vpminsd', 'fxtract', 'hint_nop2', 'setcc', 'vpcomud', 'vfmadd123sd', 'vcmpnge_uqps', 'rdpkru', 
    'cvtdq2ps', 'xrstors64', 'pclmullqhqdq', 'vcompressps', 'pfnacc', 'b.1.46', 'vmfunc', 'vexpandpd', 
    'vpmovzxwd', 'monitor', 'cpu_write', 'movdq2q', 'vfnmadd213ps', 'pmulhrwa', 'kortestq', 
    'hint_nop38', 'fsqrt', 'fxsave', 'vcmpss', 'scasq', 'iretq', 'pclmulqdq', 'pmaxud', 
    'vfmaddsub321ps', 'vroundps', 'movddup', 'vcmpneq_oqps', 'das', 'vpmaxsd', 'vphadduwq', 
    'vfnmsub312ss', 'vpmovwb', 'xor', 'vgetmantss', 'vmwrite', 'vpmovuswb', 'lmsw', 'vpmaxsw', 'btr', 
    'hlt', 'vfnmadd123pd', 'aesimc', 'vpalignr', 'vrangeps', 'vpermilps', 'sysexit', 'psubusw', 
    'vmovmskpd', 'vpaddusb', 'korw', 'hint_nop1', 'fprem', 'vmload', 'vcmpngtps', 'vcmple_osps', 
    'cmpeqpd', 'pmulhw', 'vptestnmb', 'stosd', 'vpsubq', 'lwpins', 'vpcompressb', 'vfmsubadd312pd', 
    'kaddd', 'lodsq', 'vcmpeqpd', 'vcvtss2usi', 'fldln2', 'vcmpordps', 'vcmpnle_uqps', 'cvttpd2dq', 
    'fxsave64', 'vfnmadd213ss', 'vmrun', 'sidt', 'xcryptcfb', 'cwd', 'vgatherpf0dpd', 'vprotd', 
    'knotq', 'fxam', 'popaw', 'ucomiss', 'vinserti32x8', 'fdivr', 'vpblendd', 'vfmsub123pd', 
    'pmulhuw', 'b.1.12', 'vcmpneq_oqpd', 'vcvtpd2uqq', 'ptest', 'vmovhpd', 'movzx', 'vbroadcastss', 
    'kortestw', 'smsw', 'emms', 'pavgb', 'packuswb', 'mulpd', 'shrx', 'hint_nop30', 'vcmpeq_ossd', 
    'vextracti32x4', 'vpabsw', 'vfixupimmsd', 'vfmaddsd', 'pfcmpge', 'vpsignd', 'vunpcklps', 'and', 
    'vmulps', 'vextracti128', 'ktestb', 'vcmpnle_uqpd', 'vfnmaddps', 'btc', 'fnstcw', 
    'vpbroadcastmw2d', 'vpmullq', 'movq', 'packsswb', 'xabort', 'pand', 'vptestnmw', 'pslld', 'kmovd', 
    'addsubps', 'f2xm1', 'out', 'hint_nop34', 'fsub', 'psubb', 'movsq', 'b.1.11', 'vhaddpd', 
    'vphaddbd', 'vpshldvw', 'vcmpeq_usps', 'hint_nop7', 'movshdup', 'vfmsubpd', 'vphsubwd', 'xend', 
    'vgetmantps', 'str', 'nop', 'pabsb', 'pmovsxbd', 'pdep', 'aesenc', 'vreduceps', 'fidivr', 'jmp', 
    'vcmpunord_qsd', 'sar', 'blendvps', 'vpmovb2m', 'vextractps', 'vsubpd', 'vcmpltsd', 'loadall286', 
    'blendpd', 'hint_nop0', 'vpmovw2m', 'pshufb', 'kandd', 'bb0_reset', 'pandn', 'outsb', 
    'vfnmsub231sd', 'paddd', 'vpsrlvq', 'vpinsrd', 'vmovdqa64', 'fptan', 'pmachriw', 'vprolvq', 'ud2a', 
    'vcvtss2sd', 'pfmul', 'vcmpneq_uqss', 'vcmpunord_qpd', 'sha1msg1', 'vpsravq', 'b.1.36', 'int01', 
    'rdpid', 'vpunpcklwd', 'addsd', 'vcmpfalse_oqsd', 'b.1.13', 'vpsubsw', 'punpckhwd', 'smintold', 
    'pmovzxwd', 'fstcw', 'vpmacsswd', 'b.1.33', 'vcmpneq_uqsd', 'rsldt', 'ktestq', 'vpmacssdql', 
    'andnpd', 'vpunpckldq', 'kunpckwd', 'hint_nop60', 'b.1.17', 'fneni', 'vptest', 'vcmpge_ospd', 
    'vsqrtps', 'vperm2f128', 'vcvtudq2pd', 'vinsertf64x4', 'kandnd', 'vexpandps', 'vpminuq', 
    'vfnmsub231pd', 'bextr', 'vcmpgepd', 'clac', 'vpmadcsswd', 'vpmovqb', 'vcvtdq2ps', 'movdir64b', 
    'shr', 'vfnmsub312sd', 'vpblendvb', 'vpmultishiftqb', 'vphsubbw', 'bndmk', 'pmullw', 'cmpnless', 
    'vcmpge_osps', 'ud2', 'vfmadd321ss', 'extrq', 'vgatherpf1dps', 'vcmpnlt_uqps', 'vgetexpsd', 
    'vcvttps2uqq', 'vfmaddsubps', 'vmread', 'int1', 'cvtsd2ss', 'svdc', 'vfmaddsub312pd', 'pshufhw', 
    'ftst', 'vaddsd', 'vbroadcasti128', 'ibts', 'equ', 'hint_nop9', 'cvtdq2pd', 'vpgatherqd', 'retfq', 
    'vcmple_oqsd', 'kshiftrq', 'pinsrq', 'vprold', 'vfmaddsub132ps', 'vreducepd', 'pdistib', 'pfsub', 
    'fld', 'valignq', 'cvtss2sd', 'phaddsw', 'cmppd', 'blci', 'vpblendmd', 'vdivps', 'vpsravd', 
    'addss', 'imul', 'vpavgb', 'b.1.39', 'vfixupimmps', 'fsin', 'pmovmskb', 'v4fmaddss', 
    'vcmpfalse_ossd', 'vfmaddsub123pd', 'vmovss', 'vextracti64x2', 'vcmpfalsesd', 'ptwrite', 'vaddpd', 
    'b.1.50', 'invlpga', 'palignr', 'fchs', 'cvtpd2dq', 'blcmsk', 'vcmpeqsd', 'hint_nop43', 'cmpless', 
    'clflush', 'vpminuw', 'movhlps', 'vrcp14ps', 'vcmplt_ossd', 'vpsrlvd', 'kandnw', 'vpclmullqlqdq', 
    'vpor', 'umonitor', 'jmpe', 'fcmove', 'pfadd', 'iret', 'kshiftld', 'b.1.18', 'vpcompressd', 
    'pshufd', 'les', 'vpmovsdb', 'movmskps', 'vcmptruepd', 'vbroadcastf128', 'vpslldq', 'vpbroadcastb',
    'vcvtps2ph', 'vfixupimmss', 'vgetmantpd', 'pcmpgtb', 'mulx', 'sarx', 'vfnmaddpd', 'sha256msg1', 
    'vpcmpistri', 'vpermi2ps', 'vfmsub231ps', 'pmaxsb', 'valignd', 'blcfill', 'cmpnltps', 'verr', 
    'vphsubsw', 'fisubr', 'cvtps2dq', 'vinserti64x4', 'vprotq', 'retnw', 'vpmadd52huq', 'sha1msg2', 
    'vpermi2w', 'vmptrst', 'vpmaxsb', 'vpxor', 'cmpltsd', 'vphaddd', 'fsubrp', 'vbroadcastf32x4', 
    'adox', 'mpsadbw', 'vdppd', 'vpmovsqd', 'vfnmsubpd', 'paddsiw', 'xbegin', 'vgatherdps', 
    'cmpxchg16b', 'kord', 'hint_nop42', 'roundsd', 'jrcxz', 'punpcklwd', 'vpermt2w', 'vrcp28ps', 
    'vfnmsub123ss', 'pcmpistri', 'vpshlq', 'vpmaskmovq', 'vpermt2d', 'cmp', 'cvttss2si', 'fcmovnb', 
    'vcmpge_oqpd', 'vpermi2pd', 'vinserti128', 'vpmacsdd', 'vpmadd52luq', 'pmvlzb', 'vpcmpeqb', 
    'vcvtsd2usi', 'vcomisd', 'div', 'blsr', 'vfmsub231sd', 'vshuff64x2', 'vpperm', 'sldt', 
    'vcvttps2udq', 'vcmpltps', 'vunpckhpd', 'vcmpngt_usss', 'vmovupd', 'xrstor64', 'pinsrd', 
    'fldlg2', 'psrad', 'lss', 'vfmadd132sd', 'vfmadd213ss', 'vfnmsubsd', 'vgatherqps', 'vcmpnlt_ussd', 
    'vcmpfalse_oqpd', 'hint_nop10', 'vpshuflw', 'vrsqrt14ss', 'vscatterdps', 'vpcmpud', 'blcs', 
    'minsd', 'vfnmadd321ss', 'fldcw', 'cmplepd', 'vpaddsb', 'movlpd', 'subpd', 'dec', 'pcmpestrm', 
    'fucomi', 'vpshrdvw', 'vcmpfalse_osps', 'vscatterpf1qpd', 'vpcmpgtb', 'vpsadbw', 'vfmsubadd132ps', 
    'vphaddubd', 'kshiftlq', 'vsubss', 'vcmpneqss', 'vphadduwd', 'hint_nop25', 'vmovhlps', 'lahf', 
    'cqo', 'vcmpnge_uspd', 'vcvtpd2ps', 'vfrczsd', 'clgi', 'vsqrtpd', 'fldl2e', 'vrndscalepd', 
    'vcvtqq2pd', 'cmovcc', 'dpps', 'pconfig', 'pfrcpv', 'enclv', 'vpdpbusds', 'pinsrw', 'vmovddup', 
    'phminposuw', 'vcvtps2pd', 'vrsqrt14sd', 'vmptrld', 'vandnpd', 'vcmpgtss', 'vsubsd', 'cldemote', 
    'vcmpord_qpd', 'vpsllvd', 'vfnmadd312ss', 'vcvtuqq2pd', 'vcmpeq_uqps', 'vfnmadd231pd', 'v4fnmaddss', 
    'vgatherpf0qpd', 'fclex', 'vfnmadd132ss', 'vpcomd', 'rcpps', 'paddusw', 'pcmpeqb', 'b.1.38', 'lar', 
    'skinit', 'b.1.15', 'vcmpgt_oqss', 'b.1.52', 'movdiri', 'vpermt2pd', 'vrcp28sd', 'vpcomub', 
    'pcmpeqw', 'punpcklbw', 'subsd', 'vpmulhuw', 'vcvtps2uqq', 'bb1_reset', 'vbroadcasti64x2', 
    'vinserti32x4', 'vrsqrt28ss', 'vmsave', 'vaesimc', 'b.1.7', 'vpmovzxwq', 'vfmsub123ss', 
    'vcmpunordpd', 'idiv', 'clzero', 'vinsertf32x4', 'b.1.19', 'vpcmpuw', 'cmpltpd', 'vcvtps2qq', 
    'vcmpunord_qss', 'vpmulld', 'vpsllw', 'vroundsd', 'fcmovnu', 'vcmpnlt_uspd', 'vpdpwssds', 
    'xsaveopt64', 'vcmple_oqpd', 'vpandnd', 'vfnmsub132ps', 'vfmaddps', 'fbld', 'psubw', 'vrndscaless', 
    'vfnmadd321ps', 'vfnmadd321sd', 'vfmsubaddpd', 'hint_nop23', 'cvtpi2pd', 'vrcp14ss', 'vcmpge_oqss', 
    'vcmpngt_uspd', 'vcmptrue_uqsd', 'swapgs', 'fwait', 'popfq', 'int', 'vpmacsdql', 'hint_nop29', 
    'neg', 'packusdw', 'vpxorq', 'vscatterpf0qpd', 'vprorvq', 'fucomp', 'pcmpeqq', 'vcmpeq_osss', 
    'slwpcb', 'fdiv', 'wrgsbase', 'movntdq', 'vbroadcastf64x2', 'vpshrdvd', 'popcnt', 'vmclear', 
    'vpgatherqq', 'kxnorw', 'vcmpeq_ussd', 'b.1.6', 'vpxord', 'vpclmulqdq', 'xorpd', 'movsb', 
    'vcmpnltpd', 'femms', 'wrshr', 'vcmpgesd', 'vextractf32x8', 'unpcklps', 'vpcmpd', 'wrpkru', 
    'fcmovb', 'vpsubd', 'lzcnt', 'vpblendmw', 'hint_nop47', 'vcvttps2qq', 'cvtsi2ss', 'vcmpnle_usss', 
    'vpsrad', 'bound', 'vmovaps', 'b.1.24', 'enclu', 'syscall', 'vmovsd', 'vcmpsd', 'vfnmsub321sd', 
    'cmpeqsd', 'vpmovm2q', 'pcmpistrm', 'vpermi2d', 'pmovzxdq', 'vpcmov', 'fstp', 'fdecstp', 
    'vzeroupper', 'vucomisd', 'vfnmsub213ss', 'vmpsadbw', 'hint_nop8', 'hint_nop51', 'vpermt2q', 
    'blsmsk', 'knotb', 'vpshldd', 'psubsw', 'sha256rnds2', 'gf2p8affineqb', 'pushfw', 'vfmsubaddps', 
    'vpcmpeqq', 'hint_nop53', 'vscatterpf0dpd', 'iretd', 'hint_nop17', 'movhps', 'xsha256', 'fild', 
    'vfmsub132ps', 'vpermps', 'shufps', 'movupd', 'stc', 'vrangepd', 'shrd', 'vmovdqu64', 'loope', 
    'vcmpeqps', 'vpcmpub', 'vpmovd2m', 'vpshufhw', 'vcmpord_spd', 'vfmsub213ss', 'andpd', 
    'vfpclasssd', 'vrcpps', 'fldz', 'lfs', 'pop', 'mulps', 'vaddss', 'vgetexppd', 'vfmaddsubpd', 
    'stosq', 'kshiftrw', 'gf2p8affineinvqb', 'sti', 'vcmpfalse_osss', 'vpminsq', 'vfmsubss', 
    'vshufi32x4', 'cvttps2pi', 'punpckhdq', 'movntpd', 'vrsqrt28ps', 'prefetchnta', 'vcvtpd2dq', 
    'vptestmb', 'bzhi', 'pblendw', 'vpmovqd', 'hint_nop11', 'enter', 'vfnmadd213sd', 'phsubd', 
    'vpunpckhwd', 'vcmpunordsd', 'fnstsw', 'ud1', 'rsqrtss', 'vxorps', 'b.1.34', 'vpcmpgtw', 
    'hint_nop32', 'vpmuldq', 'vcmpgt_ossd', 'divss', 'vpmovsxdq', 'vfmadd321ps', 'vpconflictd', 
    'vrcp28ss', 'vcmpneq_uqpd', 'vfpclasspd', 'maskmovdqu', 'vphaddwd', 'vpsignw', 'vfmadd231pd', 
    'vfnmsub231ps', 'fprem1', 'vfrczss', 'vcmpeq_uqpd', 'cmpnltsd', 'ficomp', 'cdq', 'vpminsb', 
    'lddqu', 'vpextrq', 'rdrand', 'vfmaddss', 'pslldq', 'hint_nop6', 'loopne', 'movntdqa', 
    'vcmpnge_uqsd', 'adcx', 'popa', 'feni', 'retfd', 'vphaddubq', 'arpl', 'invd', 'hint_nop27', 
    'movntps', 'vhsubpd', 'cmpxchg8b', 'vmovdqa32', 'andnps', 'vcmpnge_uqss', 'vfmadd123ps', 
    'cmpnltpd', 'b.1.35', 'vcmpneq_usps', 'b.1.8', 'vpshab', 'andps', 'vinsertf32x8', 'vmmcall', 
    'vcmpneq_oqss', 'vpclmullqhqdq', 'vfmsubadd213ps', 'vcmpge_oqps', 'vmovshdup', 'bndstx', 
    'vcmpunordps', 'bt', 'vpabsd', 'vfmaddsub132pd', 'vrsqrt28sd', 'korb', 'vcmpngt_uqss', 'divsd', 
    'movntsd', 'vpshrdvq', 'hint_nop35', 'vdivsd', 'vcompresspd', 'vmovdqu8', 'vpaddw', 'vlddqu', 
    'divps', 'faddp', 'vcmplt_osss', 'clwb', 'vpmaxud', 'vpshrdw', 'vfnmsub231ss', 'pminuw', 
    'vpunpckhdq', 'movmskpd', 'vpsrld', 'b.1.31', 'b.1.48', 'vfnmsub213pd', 'pabsd', 'vpsignb', 
    'vscalefpd', 'vpmovusqb', 'vcmple_oqps', 'vfmsubadd123pd', 'xcryptecb', 'vfmaddsub321pd', 
    'vhsubps', 'vpconflictq', 'prefetchw', 'hint_nop36', 'vpshldw', 'pfrsqrt', 'vfmadd321pd', 
    'kandw', 'vgatherpf1qpd', 'vcmptrueps', 'cmpleps', 'vgf2p8affineinvqb', 'vcmplt_oqpd', 
    'vaddsubpd', 'vmovdqa', 'cmpordss', 'umov', 'vcmpltpd', 'in', 'hint_nop54', 'vfmsub321ss', 
    'punpckhqdq', 'vfmadd312ss', 'cmpsw', 'stosb', 'vpminub', 'vbroadcastf64x4', 'mulsd', 'vpmacsww', 
    'rsdc', 'movlhps', 'vpcmpeqw', 'vperm2i128', 'vcmpneqpd', 'vexp2pd', 'vpclmulhqlqdq', 'vblendps', 
    'cmplesd', 'mwaitx', 'hint_nop5', 'vpopcntq', 'psllq', 'vscatterqps', 'cmpltps', 'xsaves64', 
    'cmpordsd', 'kandb', 'vcmpunord_sss', 'vscalefps', 'jcc', 'vpopcntw', 'vcmpneq_ussd', 'cmpnltss', 
    'maxpd', 'vfixupimmpd', 'vpsrlw', 'vfmsub321pd', 'pmuldq', 'movhpd', 'vpackusdw', 'cmpnlepd', 
    'vcmpgt_oqps', 'b.1.44', 'vmovsldup', 'vcmpnle_uqsd', 'vpermi2b', 'vcmpngeps', 'vcmpge_oqsd', 
    'vgatherqpd', 'retd', 'vscatterpf1qps', 'vmovlpd', 'shl', 'icebp', 'vpunpcklqdq', 'vpmovm2b', 
    'pause', 'vcmpunord_qps', 'vcmptrue_uqpd', 'finit', 'rdseed', 'clc', 'fndisi', 'vpcmpb', 
    'minss', 'vpackuswb', 'vpminud', 'pfrsqrtv', 'comiss', 'vpmadcswd', 'hsubps', 'vpcmpuq', 
    'vphadddq', 'fcmovu', 'comisd', 'vminps', 'aeskeygenassist', 'frndint', 'vpaddb', 'kxorq', 
    'vcmpnlt_uqss', 'vextracti32x8', 'orpd', 'vpsraq', 'lidt', 'pabsw', 'vcmpgt_oqpd', 'vpsllq', 
    'vmovhps', 'b.1.14', 'vhaddps', 'vstmxcsr', 'lds', 'unpckhps', 'vfmsubadd123ps', 'vcvttpd2dq', 
    'vfmaddpd', 'cmpps', 'vfmsubadd321pd', 'vcmpord_qps', 'vscatterpf0qps', 'fmulp', 
    'vscatterpf0dps', 'b.1.30', 'pmaxuw', 'b.1.40', 'xrstors', 'cmpeqss', 'vpshldvq', 'gf2p8mulb', 
    'vpdpwssd', 'vcmpnlt_usss', 'vcmpnlt_usps', 'retnd', 'fldpi', 'cmpltss', 'vpsllvq', 'vpcmpgtq', 
    'vfmsub213pd', 'pf2id', 'fisttp', 'pcmpgtw', 'kxorw', 'clts', 'vmovmskps', 'vcmptruesd', 'psraw', 
    'pusha', 'vfnmsub132pd', 'hint_nop41', 'vpmacswd', 'vfrczpd', 'vshuff32x4', 'paddsw', 
    'hint_nop3', 'vfnmadd231ps', 'rdgsbase', 'encls', 'vmcall', 'ffree', 'vblendmps', 'fimul', 
    'vfnmsubss', 'vpsrlvw', 'int3', 'vpbroadcastmb2q', 'fsubr', 'vpscatterdq', 'pminub', 'vmovqqa', 
    'kmovb', 'vpshldvd', 'leave', 'movnti', 'inc', 'vpsubsb', 'bndmov', 'vpinsrq', 'hint_nop19', 
    'pcmpgtd', 'popfd', 'vcmpngt_ussd', 'vpdpbusd', 'vcmpord_qsd', 'fmul', 'invept', 'b.1.16', 
    'vpshaq', 'vpblendmb', 'vpcmpgtd', 'vrcp14pd', 'vpermb', 'rsts', 'pcmpeqd', 'vgetexpss', 
    'pmovzxwq', 'vbroadcasti32x2', 'vandnps', 'retq', 'vcmpneq_uqps', 'wbnoinvd', 'vfmsub213ps', 
    'hint_nop39', 'movbe', 'pfrcp', 'fxrstor64', 'rdshr', 'psrld', 'fscale', 'vcmpfalsepd', 'movlps', 
    'vfmadd132ps', 'vpsubusb', 'vtestpd', 'popf', 'vmxoff', 'vfmsub132ss', 'vsubps', 'xlat', 
    'vldmxcsr', 'vexp2ps', 'add', 'vfmadd132ss', 'psadbw', 'vcmpunord_ssd', 'vcmpfalsess', 'or', 
    'pmovzxbq', 'vpcmpw', 'lldt', 'vpcomuw', 'vfmsub312pd', 'vprorq', 'hint_nop24', 'cbw', 'cvtpi2ps', 
    'vcmpneq_uspd', 'vfmsub231ss', 'hint_nop61', 'vcmpeq_uqsd', 'vprolq', 'vpextrd', 'vpaddsw', 
    'vshufps', 'b.1.47', 'hint_nop58', 'vfmadd231sd', 'vpmovsxwd', 'vphsubw', 'vphaddsw', 'getsec', 
    'vcvtpd2qq', 'xsetbv', 'vpscatterqq', 'kshiftlb', 'b.1.4', 'lea', 'vpblendmq', 'movsd', 
    'vcmpunordss', 'vpternlogd', 'fcmovne', 'cmpsd', 'mov', 'vpexpandq', 'vpmovmskb', 
    'vbroadcasti32x4', 'vcmpgess', 'vpmulhrsw', 'insd', 'b.1.26', 'mwait', 'vbroadcastf32x8', 
    'vptestnmd', 'vcmptrue_ussd', 'vpaddd', 'xsavec', 'prefetcht0', 'cvttpd2pi', 'vsqrtsd', 'vpshlb', 
    'vpopcntb', 'vcvtps2udq', 'roundss', 'vmaxsd', 'vrsqrt28pd', 'vpscatterqd', 'vcmpnlepd', 
    'vcmpnle_uqss', 'vfnmadd213pd', 'vcmple_ossd', 'vcmpneq_usss', 'vfmadd213pd', 'haddps', 
    'vfpclassps', 'vpclmulhqhqdq', 'andn', 'vpermw', 'vcmpnle_ussd', 'vpbroadcastq', 'fstsw', 
    'vdpps', 'psignb', 'vpmovusqw', 'vmovdqu16', 'vmovlps', 'vscatterpf1dps', 'pfpnacc', 'pblendvb', 
    'addsubpd', 'xadd', 'dppd', 'aesenclast', 'movsw', 'roundps', 'aesdeclast', 'fnclex', 'orps', 
    'vpgatherdq', 'fldl2t', 'pmovsxbq', 'unpckhpd', 'b.1.51', 'vmovntdqa', 'vphsubdq', 'xsaves', 
    'hint_nop62', 'std', 'vfmsub123ps', 'vfnmaddsd', 'vpermt2ps', 'vgetmantsd', 'vpmovzxbq', 
    'vcmpleps', 'vfmsub213sd', 'lodsd', 'vcmpfalseps', 'vcmpfalse_oqss', 'vpmovsxbw', 'vpermilpd', 
    'vzeroall', 'vcmplepd', 'punpcklqdq', 'vpcmpistrm', 'vpmovsqb', 'v4dpwssds', 'sqrtpd', 
    'pmuludq', 'sqrtps', 'vpmovusdw', 'prefetcht1', 'vcvtqq2ps', 'outsd', 'vfnmsub123sd', 
    'vfmadd312pd', 'vgatherpf0dps', 'minps', 'fcos', 'vfmadd123pd', 'vpshrdq', 'cmpunordsd', 
    'ud2b', 'vcmpgt_osss', 'vfmsubadd231pd', 'vpscatterdd', 'vpsllvw', 'xchg', 'vpsubw', 
    'vfnmadd231sd', 'movsxd', 'fsubp', 'vmovq', 'vextracti64x4', 'rdpmc'
]

scratch = ['rax', 'rcx', 'rdx', 'rsi', 'rdi', 'r8', 'r9', 'r10', 'r11']

class HighlighterNASM:

    colors = [
        # (start tokens, color, type, end token)

        (specialInstructions, 209),
        (['global'], 209),
        (builtins, 52),
        ('=-+*%^&|></~', 161),
        #(['0'], 11, 'till', '\n'),
        ('1234567890', 7),
        (';', 245, 'till', '\n'),
        (['section'], 161, 'till', '\n'),
        ('\"', 11, 'till', '\"'),
        ('\'', 11, 'till', '\''),
        (scratch, 12)
    ]


    def __init__(self, rules=None):
        if rules:
            self.rules = rules
        else:
            self.rules = HighlighterNASM.colors

        self.multiLineComment = None

        self.backslash = False

        self.backslashColor = 6


    def getSpecial(self, c):
        if len(c) <= 2:
            return None
        else:
            return c[1:4]


    def split(self, line):
        dividers = ' 1234567890(){}[]=+-*^%|?&<>.,:;@/~#\'\"\\'
        
        ls = []
        latest = ''
        currentDividing = False

        for char in line: 
            if char in dividers:
                if latest != '':
                    ls.append(latest)
                currentDividing = True
                latest = char
            else:
                if currentDividing:
                    currentDividing = False
                    ls.append(latest)
                    latest = ''

                latest += char

        ls.append(latest)
        return ls

    def getColors(self, line):
        ls = self.split(line)
        newLs = []

        special = None


        # f = open('debug.log', 'a')

        # t = self.rules[4][0]
        # f.write(f'update = {t}\n')

        last3 = []
        for k in ls:

            last3.append(k)
            if len(last3) > 3:
                last3.pop(0)

            if self.multiLineComment:
                # print(f'debug {last3} {special}')
                if ''.join(last3) == self.multiLineComment:
                    # print('end')
                    self.multiLineComment = None

                newLs.append((k, 11))
                continue

            # print(f'special {special} {k}')

            if special:
                type_ = special[1]
                color = special[0]

                # if type_ != 'between':
                #     newLs.append((k, special[0]))

                # char right after a backslash
                if self.backslash:
                    newLs.append((k, self.backslashColor))
                    self.backslash = False
                    continue

                # check for backslash in a string
                if k == '\\' and special == (11, 'till', '\'\"'):
                    newLs.append((k, self.backslashColor))
                    self.backslash = True
                    continue

                if k in special[2] and type_ in ['till', 'between']:
                    # end of special
                    # f.write(f'ending {special}\n')
                    special = None

                    if type_ != 'between':
                        newLs.append((k, color))
                        continue
                    else:
                        pass # between at the end (i.e. at the end token)
                else:
                    # not the end, i.e. middle section
                    newLs.append((k, color))
                    continue

            if ''.join(last3) in ['\'\'\'', '"""']: #11, 'till', '\'\"'
                # print('debug!')
                # print(last3)
                self.multiLineComment = ''.join(last3)
                special = None
                newLs.append((k, 11))
                continue

            for c in self.rules:
                if k in c[0]:
                    s = self.getSpecial(c)
                    if s:
                        assert s[1] in ['till', 'between']
                        special = s
                        # f.write(f'activating {c}, key = {k}\n')

                    if s and s[1] == 'between':
                        continue

                    newLs.append((k, c[1]))
                    break
            else:
                newLs.append((k, 16))

        # f.close()

        return newLs

    def getAllColors(self, lines):
        self.multiLineComment = None
        return [self.getColors(l) for l in lines]

if __name__ == '__main__':
    h = HighlighterNASM()
    print(h.getColors('add'))


