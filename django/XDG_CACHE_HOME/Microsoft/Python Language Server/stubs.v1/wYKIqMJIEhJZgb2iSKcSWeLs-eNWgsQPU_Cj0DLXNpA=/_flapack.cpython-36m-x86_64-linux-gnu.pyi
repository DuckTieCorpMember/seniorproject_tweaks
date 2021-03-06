__doc__ = "This module '_flapack' is auto-generated with f2py (version:2).\nFunctions:\n  a,b,alphar,alphai,beta,q,z,m,pl,pr,dif,work,iwork,info = stgsen(select,a,b,q,z,lwork=MAX(4*n+16,2*m*(n-m)),liwork=n+6,overwrite_a=0,overwrite_b=0,overwrite_q=0,overwrite_z=0)\n  a,b,alphar,alphai,beta,q,z,m,pl,pr,dif,work,iwork,info = dtgsen(select,a,b,q,z,lwork=MAX(4*n+16,2*m*(n-m)),liwork=n+6,overwrite_a=0,overwrite_b=0,overwrite_q=0,overwrite_z=0)\n  a,b,alpha,beta,q,z,m,pl,pr,dif,work,iwork,info = ctgsen(select,a,b,q,z,lwork=2*m*(n-m),liwork=n+2,overwrite_a=0,overwrite_b=0,overwrite_q=0,overwrite_z=0)\n  a,b,alpha,beta,q,z,m,pl,pr,dif,work,iwork,info = ztgsen(select,a,b,q,z,lwork=2*m*(n-m),liwork=n+2,overwrite_a=0,overwrite_b=0,overwrite_q=0,overwrite_z=0)\n  a,b,sdim,alphar,alphai,beta,vsl,vsr,work,info = sgges(sselect,a,b,jobvsl=1,jobvsr=1,sort_t=0,ldvsl=((jobvsl==1)?n:1),ldvsr=((jobvsr==1)?n:1),lwork=8*n+16,sselect_extra_args=(),overwrite_a=0,overwrite_b=0)\n  a,b,sdim,alphar,alphai,beta,vsl,vsr,work,info = dgges(dselect,a,b,jobvsl=1,jobvsr=1,sort_t=0,ldvsl=((jobvsl==1)?n:1),ldvsr=((jobvsr==1)?n:1),lwork=8*n+16,dselect_extra_args=(),overwrite_a=0,overwrite_b=0)\n  a,b,sdim,alpha,beta,vsl,vsr,work,info = cgges(cselect,a,b,jobvsl=1,jobvsr=1,sort_t=0,ldvsl=((jobvsl==1)?n:1),ldvsr=((jobvsr==1)?n:1),lwork=2*n,cselect_extra_args=(),overwrite_a=0,overwrite_b=0)\n  a,b,sdim,alpha,beta,vsl,vsr,work,info = zgges(zselect,a,b,jobvsl=1,jobvsr=1,sort_t=0,ldvsl=((jobvsl==1)?n:1),ldvsr=((jobvsr==1)?n:1),lwork=2*n,zselect_extra_args=(),overwrite_a=0,overwrite_b=0)\n  c,info = spbtrf(ab,lower=0,ldab=shape(ab,0),overwrite_ab=0)\n  c,info = dpbtrf(ab,lower=0,ldab=shape(ab,0),overwrite_ab=0)\n  c,info = cpbtrf(ab,lower=0,ldab=shape(ab,0),overwrite_ab=0)\n  c,info = zpbtrf(ab,lower=0,ldab=shape(ab,0),overwrite_ab=0)\n  x,info = spbtrs(ab,b,lower=0,ldab=shape(ab,0),overwrite_b=0)\n  x,info = dpbtrs(ab,b,lower=0,ldab=shape(ab,0),overwrite_b=0)\n  x,info = cpbtrs(ab,b,lower=0,ldab=shape(ab,0),overwrite_b=0)\n  x,info = zpbtrs(ab,b,lower=0,ldab=shape(ab,0),overwrite_b=0)\n  x,info = strtrs(a,b,lower=0,trans=0,unitdiag=0,lda=shape(a,0),overwrite_b=0)\n  x,info = dtrtrs(a,b,lower=0,trans=0,unitdiag=0,lda=shape(a,0),overwrite_b=0)\n  x,info = ctrtrs(a,b,lower=0,trans=0,unitdiag=0,lda=shape(a,0),overwrite_b=0)\n  x,info = ztrtrs(a,b,lower=0,trans=0,unitdiag=0,lda=shape(a,0),overwrite_b=0)\n  c,x,info = spbsv(ab,b,lower=0,ldab=shape(ab,0),overwrite_ab=0,overwrite_b=0)\n  c,x,info = dpbsv(ab,b,lower=0,ldab=shape(ab,0),overwrite_ab=0,overwrite_b=0)\n  c,x,info = cpbsv(ab,b,lower=0,ldab=shape(ab,0),overwrite_ab=0,overwrite_b=0)\n  c,x,info = zpbsv(ab,b,lower=0,ldab=shape(ab,0),overwrite_ab=0,overwrite_b=0)\n  d,du,x,info = sptsv(d,e,b,overwrite_d=0,overwrite_e=0,overwrite_b=0)\n  d,du,x,info = dptsv(d,e,b,overwrite_d=0,overwrite_e=0,overwrite_b=0)\n  d,du,x,info = cptsv(d,e,b,overwrite_d=0,overwrite_e=0,overwrite_b=0)\n  d,du,x,info = zptsv(d,e,b,overwrite_d=0,overwrite_e=0,overwrite_b=0)\n  ba,lo,hi,pivscale,info = sgebal(a,scale=0,permute=0,overwrite_a=0)\n  ba,lo,hi,pivscale,info = dgebal(a,scale=0,permute=0,overwrite_a=0)\n  ba,lo,hi,pivscale,info = cgebal(a,scale=0,permute=0,overwrite_a=0)\n  ba,lo,hi,pivscale,info = zgebal(a,scale=0,permute=0,overwrite_a=0)\n  ht,tau,info = sgehrd(a,lo=0,hi=n-1,lwork=MAX(n,1),overwrite_a=0)\n  ht,tau,info = dgehrd(a,lo=0,hi=n-1,lwork=MAX(n,1),overwrite_a=0)\n  ht,tau,info = cgehrd(a,lo=0,hi=n-1,lwork=MAX(n,1),overwrite_a=0)\n  ht,tau,info = zgehrd(a,lo=0,hi=n-1,lwork=MAX(n,1),overwrite_a=0)\n  work,info = sgehrd_lwork(n,lo=0,hi=n-1)\n  work,info = dgehrd_lwork(n,lo=0,hi=n-1)\n  work,info = cgehrd_lwork(n,lo=0,hi=n-1)\n  work,info = zgehrd_lwork(n,lo=0,hi=n-1)\n  ht,info = sorghr(a,tau,lo=0,hi=n-1,lwork=hi-lo,overwrite_a=0)\n  ht,info = dorghr(a,tau,lo=0,hi=n-1,lwork=hi-lo,overwrite_a=0)\n  work,info = sorghr_lwork(n,lo=0,hi=n-1)\n  work,info = dorghr_lwork(n,lo=0,hi=n-1)\n  ht,info = cunghr(a,tau,lo=0,hi=n-1,lwork=hi-lo,overwrite_a=0)\n  ht,info = zunghr(a,tau,lo=0,hi=n-1,lwork=hi-lo,overwrite_a=0)\n  work,info = cunghr_lwork(n,lo=0,hi=n-1)\n  work,info = zunghr_lwork(n,lo=0,hi=n-1)\n  lub,piv,x,info = sgbsv(kl,ku,ab,b,overwrite_ab=0,overwrite_b=0)\n  lub,piv,x,info = dgbsv(kl,ku,ab,b,overwrite_ab=0,overwrite_b=0)\n  lub,piv,x,info = cgbsv(kl,ku,ab,b,overwrite_ab=0,overwrite_b=0)\n  lub,piv,x,info = zgbsv(kl,ku,ab,b,overwrite_ab=0,overwrite_b=0)\n  du2,d,du,x,info = sgtsv(dl,d,du,b,overwrite_dl=0,overwrite_d=0,overwrite_du=0,overwrite_b=0)\n  du2,d,du,x,info = dgtsv(dl,d,du,b,overwrite_dl=0,overwrite_d=0,overwrite_du=0,overwrite_b=0)\n  du2,d,du,x,info = cgtsv(dl,d,du,b,overwrite_dl=0,overwrite_d=0,overwrite_du=0,overwrite_b=0)\n  du2,d,du,x,info = zgtsv(dl,d,du,b,overwrite_dl=0,overwrite_d=0,overwrite_du=0,overwrite_b=0)\n  lu,piv,x,info = sgesv(a,b,overwrite_a=0,overwrite_b=0)\n  lu,piv,x,info = dgesv(a,b,overwrite_a=0,overwrite_b=0)\n  lu,piv,x,info = cgesv(a,b,overwrite_a=0,overwrite_b=0)\n  lu,piv,x,info = zgesv(a,b,overwrite_a=0,overwrite_b=0)\n  as,lu,ipiv,equed,rs,cs,bs,x,rcond,ferr,berr,info = sgesvx(a,b,fact='E',trans='N',af=,ipiv=,equed='B',r=,c=,overwrite_a=0,overwrite_b=0)\n  as,lu,ipiv,equed,rs,cs,bs,x,rcond,ferr,berr,info = dgesvx(a,b,fact='E',trans='N',af=,ipiv=,equed='B',r=,c=,overwrite_a=0,overwrite_b=0)\n  as,lu,ipiv,equed,rs,cs,bs,x,rcond,ferr,berr,info = cgesvx(a,b,fact='E',trans='N',af=,ipiv=,equed='B',r=,c=,overwrite_a=0,overwrite_b=0)\n  as,lu,ipiv,equed,rs,cs,bs,x,rcond,ferr,berr,info = zgesvx(a,b,fact='E',trans='N',af=,ipiv=,equed='B',r=,c=,overwrite_a=0,overwrite_b=0)\n  rcond,info = sgecon(a,anorm,norm='1')\n  rcond,info = dgecon(a,anorm,norm='1')\n  rcond,info = cgecon(a,anorm,norm='1')\n  rcond,info = zgecon(a,anorm,norm='1')\n  udut,ipiv,x,info = ssysv(a,b,lwork=n,lower=0,overwrite_a=0,overwrite_b=0)\n  udut,ipiv,x,info = dsysv(a,b,lwork=n,lower=0,overwrite_a=0,overwrite_b=0)\n  udut,ipiv,x,info = csysv(a,b,lwork=n,lower=0,overwrite_a=0,overwrite_b=0)\n  udut,ipiv,x,info = zsysv(a,b,lwork=n,lower=0,overwrite_a=0,overwrite_b=0)\n  work,info = ssysv_lwork(n,lower=0)\n  work,info = dsysv_lwork(n,lower=0)\n  work,info = csysv_lwork(n,lower=0)\n  work,info = zsysv_lwork(n,lower=0)\n  a_s,udut,ipiv,b_s,x,rcond,ferr,berr,info = ssysvx(a,b,af=,ipiv=,lwork=3*n,factored=0,lower=0,overwrite_a=0,overwrite_b=0)\n  a_s,udut,ipiv,b_s,x,rcond,ferr,berr,info = dsysvx(a,b,af=,ipiv=,lwork=3*n,factored=0,lower=0,overwrite_a=0,overwrite_b=0)\n  a_s,udut,ipiv,b_s,x,rcond,ferr,berr,info = csysvx(a,b,af=,ipiv=,lwork=3*n,factored=0,lower=0,overwrite_a=0,overwrite_b=0)\n  a_s,udut,ipiv,b_s,x,rcond,ferr,berr,info = zsysvx(a,b,af=,ipiv=,lwork=3*n,factored=0,lower=0,overwrite_a=0,overwrite_b=0)\n  work,info = ssysvx_lwork(n,lower=0)\n  work,info = dsysvx_lwork(n,lower=0)\n  work,info = csysvx_lwork(n,lower=0)\n  work,info = zsysvx_lwork(n,lower=0)\n  uduh,ipiv,x,info = chesv(a,b,lwork=n,lower=0,overwrite_a=0,overwrite_b=0)\n  uduh,ipiv,x,info = zhesv(a,b,lwork=n,lower=0,overwrite_a=0,overwrite_b=0)\n  work,info = chesv_lwork(n,lower=0)\n  work,info = zhesv_lwork(n,lower=0)\n  uduh,ipiv,x,rcond,ferr,berr,info = chesvx(a,b,af=,ipiv=,lwork=2*n,factored=0,lower=0,overwrite_a=0,overwrite_b=0)\n  uduh,ipiv,x,rcond,ferr,berr,info = zhesvx(a,b,af=,ipiv=,lwork=2*n,factored=0,lower=0,overwrite_a=0,overwrite_b=0)\n  work,info = chesvx_lwork(n,lower=0)\n  work,info = zhesvx_lwork(n,lower=0)\n  lu,piv,info = sgetrf(a,overwrite_a=0)\n  lu,piv,info = dgetrf(a,overwrite_a=0)\n  lu,piv,info = cgetrf(a,overwrite_a=0)\n  lu,piv,info = zgetrf(a,overwrite_a=0)\n  x,info = sgetrs(lu,piv,b,trans=0,overwrite_b=0)\n  x,info = dgetrs(lu,piv,b,trans=0,overwrite_b=0)\n  x,info = cgetrs(lu,piv,b,trans=0,overwrite_b=0)\n  x,info = zgetrs(lu,piv,b,trans=0,overwrite_b=0)\n  inv_a,info = sgetri(lu,piv,lwork=3*n,overwrite_lu=0)\n  inv_a,info = dgetri(lu,piv,lwork=3*n,overwrite_lu=0)\n  inv_a,info = cgetri(lu,piv,lwork=3*n,overwrite_lu=0)\n  inv_a,info = zgetri(lu,piv,lwork=3*n,overwrite_lu=0)\n  work,info = sgetri_lwork(n)\n  work,info = dgetri_lwork(n)\n  work,info = cgetri_lwork(n)\n  work,info = zgetri_lwork(n)\n  u,s,vt,info = sgesdd(a,compute_uv=1,full_matrices=1,lwork=(compute_uv?4*minmn*minmn+MAX(m,n)+9*minmn:MAX(14*minmn+4,10*minmn+2+25*(25+8))+MAX(m,n)),overwrite_a=0)\n  u,s,vt,info = dgesdd(a,compute_uv=1,full_matrices=1,lwork=(compute_uv?4*minmn*minmn+MAX(m,n)+9*minmn:MAX(14*minmn+4,10*minmn+2+25*(25+8))+MAX(m,n)),overwrite_a=0)\n  work,info = sgesdd_lwork(m,n,compute_uv=1,full_matrices=1)\n  work,info = dgesdd_lwork(m,n,compute_uv=1,full_matrices=1)\n  u,s,vt,info = cgesdd(a,compute_uv=1,full_matrices=1,lwork=(compute_uv?2*minmn*minmn+MAX(m,n)+2*minmn:2*minmn+MAX(m,n)),overwrite_a=0)\n  u,s,vt,info = zgesdd(a,compute_uv=1,full_matrices=1,lwork=(compute_uv?2*minmn*minmn+MAX(m,n)+2*minmn:2*minmn+MAX(m,n)),overwrite_a=0)\n  work,info = cgesdd_lwork(m,n,compute_uv=1,full_matrices=1)\n  work,info = zgesdd_lwork(m,n,compute_uv=1,full_matrices=1)\n  u,s,vt,info = sgesvd(a,compute_uv=1,full_matrices=1,lwork=MAX(1,MAX(3*minmn+MAX(m,n),5*minmn)),overwrite_a=0)\n  u,s,vt,info = dgesvd(a,compute_uv=1,full_matrices=1,lwork=MAX(1,MAX(3*minmn+MAX(m,n),5*minmn)),overwrite_a=0)\n  work,info = sgesvd_lwork(m,n,compute_uv=1,full_matrices=1)\n  work,info = dgesvd_lwork(m,n,compute_uv=1,full_matrices=1)\n  u,s,vt,info = cgesvd(a,compute_uv=1,full_matrices=1,lwork=MAX(1,2*minmn+MAX(m,n)),overwrite_a=0)\n  u,s,vt,info = zgesvd(a,compute_uv=1,full_matrices=1,lwork=MAX(1,2*minmn+MAX(m,n)),overwrite_a=0)\n  work,info = cgesvd_lwork(m,n,compute_uv=1,full_matrices=1)\n  work,info = zgesvd_lwork(m,n,compute_uv=1,full_matrices=1)\n  v,x,s,rank,work,info = sgelss(a,b,cond=-1.0,lwork=3*minmn+MAX(2*minmn,MAX(maxmn,nrhs)),overwrite_a=0,overwrite_b=0)\n  v,x,s,rank,work,info = dgelss(a,b,cond=-1.0,lwork=3*minmn+MAX(2*minmn,MAX(maxmn,nrhs)),overwrite_a=0,overwrite_b=0)\n  work,info = sgelss_lwork(m,n,nrhs,cond=-1.0,lwork=-1)\n  work,info = dgelss_lwork(m,n,nrhs,cond=-1.0,lwork=-1)\n  v,x,s,rank,work,info = cgelss(a,b,cond=-1.0,lwork=2*minmn+MAX(maxmn,nrhs),overwrite_a=0,overwrite_b=0)\n  v,x,s,rank,work,info = zgelss(a,b,cond=-1.0,lwork=2*minmn+MAX(maxmn,nrhs),overwrite_a=0,overwrite_b=0)\n  delta,sigma,work,info = slasd4(i,d,z,rho=1.0)\n  delta,sigma,work,info = dlasd4(i,d,z,rho=1.0)\n  work,info = cgelss_lwork(m,n,nrhs,cond=-1.0,lwork=-1)\n  work,info = zgelss_lwork(m,n,nrhs,cond=-1.0,lwork=-1)\n  v,x,j,rank,info = sgelsy(a,b,jptv,cond,lwork,overwrite_a=0,overwrite_b=0)\n  v,x,j,rank,info = dgelsy(a,b,jptv,cond,lwork,overwrite_a=0,overwrite_b=0)\n  work,info = sgelsy_lwork(m,n,nrhs,cond,lwork=-1)\n  work,info = dgelsy_lwork(m,n,nrhs,cond,lwork=-1)\n  v,x,j,rank,info = cgelsy(a,b,jptv,cond,lwork,overwrite_a=0,overwrite_b=0)\n  v,x,j,rank,info = zgelsy(a,b,jptv,cond,lwork,overwrite_a=0,overwrite_b=0)\n  work,info = cgelsy_lwork(m,n,nrhs,cond,lwork=-1)\n  work,info = zgelsy_lwork(m,n,nrhs,cond,lwork=-1)\n  x,s,rank,info = sgelsd(a,b,lwork,size_iwork,cond=-1.0,overwrite_a=0,overwrite_b=0)\n  x,s,rank,info = dgelsd(a,b,lwork,size_iwork,cond=-1.0,overwrite_a=0,overwrite_b=0)\n  work,iwork,info = sgelsd_lwork(m,n,nrhs,cond=-1.0,lwork=-1)\n  work,iwork,info = dgelsd_lwork(m,n,nrhs,cond=-1.0,lwork=-1)\n  x,s,rank,info = cgelsd(a,b,lwork,size_rwork,size_iwork,cond=-1.0,overwrite_a=0,overwrite_b=0)\n  x,s,rank,info = zgelsd(a,b,lwork,size_rwork,size_iwork,cond=-1.0,overwrite_a=0,overwrite_b=0)\n  work,rwork,iwork,info = cgelsd_lwork(m,n,nrhs,cond=-1.0,lwork=-1)\n  work,rwork,iwork,info = zgelsd_lwork(m,n,nrhs,cond=-1.0,lwork=-1)\n  qr,jpvt,tau,work,info = sgeqp3(a,lwork=3*(n+1),overwrite_a=0)\n  qr,jpvt,tau,work,info = dgeqp3(a,lwork=3*(n+1),overwrite_a=0)\n  qr,jpvt,tau,work,info = cgeqp3(a,lwork=3*(n+1),overwrite_a=0)\n  qr,jpvt,tau,work,info = zgeqp3(a,lwork=3*(n+1),overwrite_a=0)\n  qr,tau,work,info = sgeqrf(a,lwork=3*n,overwrite_a=0)\n  qr,tau,work,info = dgeqrf(a,lwork=3*n,overwrite_a=0)\n  qr,tau,work,info = cgeqrf(a,lwork=3*n,overwrite_a=0)\n  qr,tau,work,info = zgeqrf(a,lwork=3*n,overwrite_a=0)\n  qr,tau,work,info = sgerqf(a,lwork=3*m,overwrite_a=0)\n  qr,tau,work,info = dgerqf(a,lwork=3*m,overwrite_a=0)\n  qr,tau,work,info = cgerqf(a,lwork=3*m,overwrite_a=0)\n  qr,tau,work,info = zgerqf(a,lwork=3*m,overwrite_a=0)\n  q,work,info = sorgqr(a,tau,lwork=3*n,overwrite_a=0)\n  q,work,info = dorgqr(a,tau,lwork=3*n,overwrite_a=0)\n  q,work,info = cungqr(a,tau,lwork=3*n,overwrite_a=0)\n  q,work,info = zungqr(a,tau,lwork=3*n,overwrite_a=0)\n  cq,work,info = sormqr(side,trans,a,tau,c,lwork,overwrite_c=0)\n  cq,work,info = dormqr(side,trans,a,tau,c,lwork,overwrite_c=0)\n  cq,work,info = cunmqr(side,trans,a,tau,c,lwork,overwrite_c=0)\n  cq,work,info = zunmqr(side,trans,a,tau,c,lwork,overwrite_c=0)\n  q,work,info = sorgrq(a,tau,lwork=3*m,overwrite_a=0)\n  q,work,info = dorgrq(a,tau,lwork=3*m,overwrite_a=0)\n  q,work,info = cungrq(a,tau,lwork=3*m,overwrite_a=0)\n  q,work,info = zungrq(a,tau,lwork=3*m,overwrite_a=0)\n  wr,wi,vl,vr,info = sgeev(a,compute_vl=1,compute_vr=1,lwork=4*n,overwrite_a=0)\n  wr,wi,vl,vr,info = dgeev(a,compute_vl=1,compute_vr=1,lwork=4*n,overwrite_a=0)\n  work,info = sgeev_lwork(n,compute_vl=1,compute_vr=1)\n  work,info = dgeev_lwork(n,compute_vl=1,compute_vr=1)\n  w,vl,vr,info = cgeev(a,compute_vl=1,compute_vr=1,lwork=2*n,overwrite_a=0)\n  w,vl,vr,info = zgeev(a,compute_vl=1,compute_vr=1,lwork=2*n,overwrite_a=0)\n  work,info = cgeev_lwork(n,compute_vl=1,compute_vr=1)\n  work,info = zgeev_lwork(n,compute_vl=1,compute_vr=1)\n  alphar,alphai,beta,vl,vr,info = sgegv(a,b,compute_vl=1,compute_vr=1,lwork=8*n,overwrite_a=0,overwrite_b=0)\n  alphar,alphai,beta,vl,vr,info = dgegv(a,b,compute_vl=1,compute_vr=1,lwork=8*n,overwrite_a=0,overwrite_b=0)\n  alpha,beta,vl,vr,info = cgegv(a,b,compute_vl=1,compute_vr=1,lwork=2*n,overwrite_a=0,overwrite_b=0)\n  alpha,beta,vl,vr,info = zgegv(a,b,compute_vl=1,compute_vr=1,lwork=2*n,overwrite_a=0,overwrite_b=0)\n  w,v,info = ssyev(a,compute_v=1,lower=0,lwork=3*n-1,overwrite_a=0)\n  w,v,info = dsyev(a,compute_v=1,lower=0,lwork=3*n-1,overwrite_a=0)\n  w,v,info = cheev(a,compute_v=1,lower=0,lwork=2*n-1,overwrite_a=0)\n  w,v,info = zheev(a,compute_v=1,lower=0,lwork=2*n-1,overwrite_a=0)\n  w,v,info = ssyevd(a,compute_v=1,lower=0,lwork=(compute_v?1+6*n+2*n*n:2*n+1),overwrite_a=0)\n  w,v,info = dsyevd(a,compute_v=1,lower=0,lwork=(compute_v?1+6*n+2*n*n:2*n+1),overwrite_a=0)\n  w,v,info = cheevd(a,compute_v=1,lower=0,lwork=(compute_v?2*n+n*n:n+1),overwrite_a=0)\n  w,v,info = zheevd(a,compute_v=1,lower=0,lwork=(compute_v?2*n+n*n:n+1),overwrite_a=0)\n  c,x,info = sposv(a,b,lower=0,overwrite_a=0,overwrite_b=0)\n  c,x,info = dposv(a,b,lower=0,overwrite_a=0,overwrite_b=0)\n  c,x,info = cposv(a,b,lower=0,overwrite_a=0,overwrite_b=0)\n  c,x,info = zposv(a,b,lower=0,overwrite_a=0,overwrite_b=0)\n  a_s,lu,equed,s,b_s,x,rcond,ferr,berr,info = sposvx(a,b,fact='E',af=,equed='Y',s=,lower=0,overwrite_a=0,overwrite_b=0)\n  a_s,lu,equed,s,b_s,x,rcond,ferr,berr,info = dposvx(a,b,fact='E',af=,equed='Y',s=,lower=0,overwrite_a=0,overwrite_b=0)\n  a_s,lu,equed,s,b_s,x,rcond,ferr,berr,info = cposvx(a,b,fact='E',af=,equed='Y',s=,lower=0,overwrite_a=0,overwrite_b=0)\n  a_s,lu,equed,s,b_s,x,rcond,ferr,berr,info = zposvx(a,b,fact='E',af=,equed='Y',s=,lower=0,overwrite_a=0,overwrite_b=0)\n  rcond,info = spocon(a,anorm,uplo='U')\n  rcond,info = dpocon(a,anorm,uplo='U')\n  rcond,info = cpocon(a,anorm,uplo='U')\n  rcond,info = zpocon(a,anorm,uplo='U')\n  c,info = spotrf(a,lower=0,clean=1,overwrite_a=0)\n  c,info = dpotrf(a,lower=0,clean=1,overwrite_a=0)\n  c,info = cpotrf(a,lower=0,clean=1,overwrite_a=0)\n  c,info = zpotrf(a,lower=0,clean=1,overwrite_a=0)\n  x,info = spotrs(c,b,lower=0,overwrite_b=0)\n  x,info = dpotrs(c,b,lower=0,overwrite_b=0)\n  x,info = cpotrs(c,b,lower=0,overwrite_b=0)\n  x,info = zpotrs(c,b,lower=0,overwrite_b=0)\n  inv_a,info = spotri(c,lower=0,overwrite_c=0)\n  inv_a,info = dpotri(c,lower=0,overwrite_c=0)\n  inv_a,info = cpotri(c,lower=0,overwrite_c=0)\n  inv_a,info = zpotri(c,lower=0,overwrite_c=0)\n  a,info = slauum(c,lower=0,overwrite_c=0)\n  a,info = dlauum(c,lower=0,overwrite_c=0)\n  a,info = clauum(c,lower=0,overwrite_c=0)\n  a,info = zlauum(c,lower=0,overwrite_c=0)\n  inv_c,info = strtri(c,lower=0,unitdiag=0,overwrite_c=0)\n  inv_c,info = dtrtri(c,lower=0,unitdiag=0,overwrite_c=0)\n  inv_c,info = ctrtri(c,lower=0,unitdiag=0,overwrite_c=0)\n  inv_c,info = ztrtri(c,lower=0,unitdiag=0,overwrite_c=0)\n  x,scale,info = strsyl(a,b,c,trana='N',tranb='N',isgn=1,overwrite_c=0)\n  x,scale,info = dtrsyl(a,b,c,trana='N',tranb='N',isgn=1,overwrite_c=0)\n  x,scale,info = ctrsyl(a,b,c,trana='N',tranb='N',isgn=1,overwrite_c=0)\n  x,scale,info = ztrsyl(a,b,c,trana='N',tranb='N',isgn=1,overwrite_c=0)\n  a = slaswp(a,piv,k1=0,k2=len(piv)-1,off=0,inc=1,overwrite_a=0)\n  a = dlaswp(a,piv,k1=0,k2=len(piv)-1,off=0,inc=1,overwrite_a=0)\n  a = claswp(a,piv,k1=0,k2=len(piv)-1,off=0,inc=1,overwrite_a=0)\n  a = zlaswp(a,piv,k1=0,k2=len(piv)-1,off=0,inc=1,overwrite_a=0)\n  t,sdim,w,vs,work,info = cgees(cselect,a,compute_v=1,sort_t=0,lwork=3*n,cselect_extra_args=(),overwrite_a=0)\n  t,sdim,w,vs,work,info = zgees(zselect,a,compute_v=1,sort_t=0,lwork=3*n,zselect_extra_args=(),overwrite_a=0)\n  t,sdim,wr,wi,vs,work,info = sgees(sselect,a,compute_v=1,sort_t=0,lwork=3*n,sselect_extra_args=(),overwrite_a=0)\n  t,sdim,wr,wi,vs,work,info = dgees(dselect,a,compute_v=1,sort_t=0,lwork=3*n,dselect_extra_args=(),overwrite_a=0)\n  alphar,alphai,beta,vl,vr,work,info = sggev(a,b,compute_vl=1,compute_vr=1,lwork=8*n,overwrite_a=0,overwrite_b=0)\n  alphar,alphai,beta,vl,vr,work,info = dggev(a,b,compute_vl=1,compute_vr=1,lwork=8*n,overwrite_a=0,overwrite_b=0)\n  alpha,beta,vl,vr,work,info = cggev(a,b,compute_vl=1,compute_vr=1,lwork=2*n,overwrite_a=0,overwrite_b=0)\n  alpha,beta,vl,vr,work,info = zggev(a,b,compute_vl=1,compute_vr=1,lwork=2*n,overwrite_a=0,overwrite_b=0)\n  w,z,info = ssbev(ab,compute_v=1,lower=0,ldab=shape(ab,0),overwrite_ab=1)\n  w,z,info = dsbev(ab,compute_v=1,lower=0,ldab=shape(ab,0),overwrite_ab=1)\n  w,z,info = ssbevd(ab,compute_v=1,lower=0,ldab=shape(ab,0),liwork=(compute_v?3+5*n:1),overwrite_ab=1)\n  w,z,info = dsbevd(ab,compute_v=1,lower=0,ldab=shape(ab,0),liwork=(compute_v?3+5*n:1),overwrite_ab=1)\n  w,z,m,ifail,info = ssbevx(ab,vl,vu,il,iu,ldab=shape(ab,0),compute_v=1,range=0,lower=0,abstol=0.0,mmax=(compute_v?(range==2?(iu-il+1):n):1),overwrite_ab=1)\n  w,z,m,ifail,info = dsbevx(ab,vl,vu,il,iu,ldab=shape(ab,0),compute_v=1,range=0,lower=0,abstol=0.0,mmax=(compute_v?(range==2?(iu-il+1):n):1),overwrite_ab=1)\n  w,z,info = chbevd(ab,compute_v=1,lower=0,ldab=shape(ab,0),lrwork=(compute_v?1+5*n+2*n*n:n),liwork=(compute_v?3+5*n:1),overwrite_ab=1)\n  w,z,info = zhbevd(ab,compute_v=1,lower=0,ldab=shape(ab,0),lrwork=(compute_v?1+5*n+2*n*n:n),liwork=(compute_v?3+5*n:1),overwrite_ab=1)\n  w,z,m,ifail,info = chbevx(ab,vl,vu,il,iu,ldab=shape(ab,0),compute_v=1,range=0,lower=0,abstol=0.0,mmax=(compute_v?(range==2?(iu-il+1):n):1),overwrite_ab=1)\n  w,z,m,ifail,info = zhbevx(ab,vl,vu,il,iu,ldab=shape(ab,0),compute_v=1,range=0,lower=0,abstol=0.0,mmax=(compute_v?(range==2?(iu-il+1):n):1),overwrite_ab=1)\n  dlamch = dlamch(cmach)\n  slamch = slamch(cmach)\n  lu,ipiv,info = sgbtrf(ab,kl,ku,m=shape(ab,1),n=shape(ab,1),ldab=shape(ab,0),overwrite_ab=0)\n  lu,ipiv,info = dgbtrf(ab,kl,ku,m=shape(ab,1),n=shape(ab,1),ldab=shape(ab,0),overwrite_ab=0)\n  lu,ipiv,info = cgbtrf(ab,kl,ku,m=shape(ab,1),n=shape(ab,1),ldab=shape(ab,0),overwrite_ab=0)\n  lu,ipiv,info = zgbtrf(ab,kl,ku,m=shape(ab,1),n=shape(ab,1),ldab=shape(ab,0),overwrite_ab=0)\n  x,info = sgbtrs(ab,kl,ku,b,ipiv,trans=0,n=shape(ab,1),ldab=shape(ab,0),ldb=shape(b,0),overwrite_b=0)\n  x,info = dgbtrs(ab,kl,ku,b,ipiv,trans=0,n=shape(ab,1),ldab=shape(ab,0),ldb=shape(b,0),overwrite_b=0)\n  x,info = cgbtrs(ab,kl,ku,b,ipiv,trans=0,n=shape(ab,1),ldab=shape(ab,0),ldb=shape(b,0),overwrite_b=0)\n  x,info = zgbtrs(ab,kl,ku,b,ipiv,trans=0,n=shape(ab,1),ldab=shape(ab,0),ldb=shape(b,0),overwrite_b=0)\n  w,z,info = ssyevr(a,jobz='V',range='A',uplo='L',il=1,iu=n,lwork=26*n,overwrite_a=0)\n  w,z,info = dsyevr(a,jobz='V',range='A',uplo='L',il=1,iu=n,lwork=26*n,overwrite_a=0)\n  w,z,info = cheevr(a,jobz='V',range='A',uplo='L',il=1,iu=n,lwork=18*n,overwrite_a=0)\n  w,z,info = zheevr(a,jobz='V',range='A',uplo='L',il=1,iu=n,lwork=18*n,overwrite_a=0)\n  a,w,info = ssygv(a,b,itype=1,jobz='V',uplo='L',overwrite_a=0,overwrite_b=0)\n  a,w,info = dsygv(a,b,itype=1,jobz='V',uplo='L',overwrite_a=0,overwrite_b=0)\n  a,w,info = chegv(a,b,itype=1,jobz='V',uplo='L',overwrite_a=0,overwrite_b=0)\n  a,w,info = zhegv(a,b,itype=1,jobz='V',uplo='L',overwrite_a=0,overwrite_b=0)\n  a,w,info = ssygvd(a,b,itype=1,jobz='V',uplo='L',lwork=1+6*n+2*n*n,overwrite_a=0,overwrite_b=0)\n  a,w,info = dsygvd(a,b,itype=1,jobz='V',uplo='L',lwork=1+6*n+2*n*n,overwrite_a=0,overwrite_b=0)\n  a,w,info = chegvd(a,b,itype=1,jobz='V',uplo='L',lwork=2*n+n*n,overwrite_a=0,overwrite_b=0)\n  a,w,info = zhegvd(a,b,itype=1,jobz='V',uplo='L',lwork=2*n+n*n,overwrite_a=0,overwrite_b=0)\n  w,z,ifail,info = ssygvx(a,b,iu,itype=1,jobz='V',uplo='L',il=1,lwork=8*n,overwrite_a=0,overwrite_b=0)\n  w,z,ifail,info = dsygvx(a,b,iu,itype=1,jobz='V',uplo='L',il=1,lwork=8*n,overwrite_a=0,overwrite_b=0)\n  w,z,ifail,info = chegvx(a,b,iu,itype=1,jobz='V',uplo='L',il=1,lwork=18*n-1,overwrite_a=0,overwrite_b=0)\n  w,z,ifail,info = zhegvx(a,b,iu,itype=1,jobz='V',uplo='L',il=1,lwork=18*n-1,overwrite_a=0,overwrite_b=0)\n  n2 = slange(norm,a)\n  n2 = dlange(norm,a)\n  n2 = clange(norm,a)\n  n2 = zlange(norm,a)\n  alpha,x,tau = slarfg(n,alpha,x,incx=1,overwrite_x=0)\n  alpha,x,tau = dlarfg(n,alpha,x,incx=1,overwrite_x=0)\n  alpha,x,tau = clarfg(n,alpha,x,incx=1,overwrite_x=0)\n  alpha,x,tau = zlarfg(n,alpha,x,incx=1,overwrite_x=0)\n  c = slarf(v,tau,c,work,side='L',incv=1,overwrite_c=0)\n  c = dlarf(v,tau,c,work,side='L',incv=1,overwrite_c=0)\n  c = clarf(v,tau,c,work,side='L',incv=1,overwrite_c=0)\n  c = zlarf(v,tau,c,work,side='L',incv=1,overwrite_c=0)\n  cs,sn,r = slartg(f,g)\n  cs,sn,r = dlartg(f,g)\n  cs,sn,r = clartg(f,g)\n  cs,sn,r = zlartg(f,g)\n  x,y = crot(x,y,c,s,n=(len(x)-1-offx)/abs(incx)+1,offx=0,incx=1,offy=0,incy=1,overwrite_x=0,overwrite_y=0)\n  x,y = zrot(x,y,c,s,n=(len(x)-1-offx)/abs(incx)+1,offx=0,incx=1,offy=0,incy=1,overwrite_x=0,overwrite_y=0)\n  major,minor,patch = ilaver()\n."
__file__ = '/usr/lib/python3/dist-packages/scipy/linalg/_flapack.cpython-36m-x86_64-linux-gnu.so'
__name__ = 'scipy.linalg._flapack'
__package__ = 'scipy.linalg'
__version__ = b'$Revision: $'
def cgbsv():
    "lub,piv,x,info = cgbsv(kl,ku,ab,b,[overwrite_ab,overwrite_b])\n\nWrapper for ``cgbsv``.\n\nParameters\n----------\nkl : input int\nku : input int\nab : input rank-2 array('F') with bounds (2*kl+ku+1,n)\nb : input rank-2 array('F') with bounds (n,nrhs)\n\nOther Parameters\n----------------\noverwrite_ab : input int, optional\n    Default: 0\noverwrite_b : input int, optional\n    Default: 0\n\nReturns\n-------\nlub : rank-2 array('F') with bounds (2*kl+ku+1,n) and ab storage\npiv : rank-1 array('i') with bounds (n)\nx : rank-2 array('F') with bounds (n,nrhs) and b storage\ninfo : int\n"
    pass

def cgbtrf():
    "lu,ipiv,info = cgbtrf(ab,kl,ku,[m,n,ldab,overwrite_ab])\n\nWrapper for ``cgbtrf``.\n\nParameters\n----------\nab : input rank-2 array('F') with bounds (ldab,*)\nkl : input int\nku : input int\n\nOther Parameters\n----------------\nm : input int, optional\n    Default: shape(ab,1)\nn : input int, optional\n    Default: shape(ab,1)\noverwrite_ab : input int, optional\n    Default: 0\nldab : input int, optional\n    Default: shape(ab,0)\n\nReturns\n-------\nlu : rank-2 array('F') with bounds (ldab,*) and ab storage\nipiv : rank-1 array('i') with bounds (MIN(m,n))\ninfo : int\n"
    pass

def cgbtrs():
    "x,info = cgbtrs(ab,kl,ku,b,ipiv,[trans,n,ldab,ldb,overwrite_b])\n\nWrapper for ``cgbtrs``.\n\nParameters\n----------\nab : input rank-2 array('F') with bounds (ldab,n)\nkl : input int\nku : input int\nb : input rank-2 array('F') with bounds (ldb,nrhs)\nipiv : input rank-1 array('i') with bounds (n)\n\nOther Parameters\n----------------\noverwrite_b : input int, optional\n    Default: 0\ntrans : input int, optional\n    Default: 0\nn : input int, optional\n    Default: shape(ab,1)\nldab : input int, optional\n    Default: shape(ab,0)\nldb : input int, optional\n    Default: shape(b,0)\n\nReturns\n-------\nx : rank-2 array('F') with bounds (ldb,nrhs) and b storage\ninfo : int\n"
    pass

def cgebal():
    "ba,lo,hi,pivscale,info = cgebal(a,[scale,permute,overwrite_a])\n\nWrapper for ``cgebal``.\n\nParameters\n----------\na : input rank-2 array('F') with bounds (m,n)\n\nOther Parameters\n----------------\nscale : input int, optional\n    Default: 0\npermute : input int, optional\n    Default: 0\noverwrite_a : input int, optional\n    Default: 0\n\nReturns\n-------\nba : rank-2 array('F') with bounds (m,n) and a storage\nlo : int\nhi : int\npivscale : rank-1 array('f') with bounds (n)\ninfo : int\n"
    pass

def cgecon():
    "rcond,info = cgecon(a,anorm,[norm])\n\nWrapper for ``cgecon``.\n\nParameters\n----------\na : input rank-2 array('F') with bounds (n,n)\nanorm : input float\n\nOther Parameters\n----------------\nnorm : input string(len=1), optional\n    Default: '1'\n\nReturns\n-------\nrcond : float\ninfo : int\n"
    pass

def cgees():
    "t,sdim,w,vs,work,info = cgees(cselect,a,[compute_v,sort_t,lwork,cselect_extra_args,overwrite_a])\n\nWrapper for ``cgees``.\n\nParameters\n----------\ncselect : call-back function\na : input rank-2 array('F') with bounds (n,n)\n\nOther Parameters\n----------------\ncompute_v : input int, optional\n    Default: 1\nsort_t : input int, optional\n    Default: 0\ncselect_extra_args : input tuple, optional\n    Default: ()\noverwrite_a : input int, optional\n    Default: 0\nlwork : input int, optional\n    Default: 3*n\n\nReturns\n-------\nt : rank-2 array('F') with bounds (n,n) and a storage\nsdim : int\nw : rank-1 array('F') with bounds (n)\nvs : rank-2 array('F') with bounds (ldvs,n)\nwork : rank-1 array('F') with bounds (MAX(lwork,1))\ninfo : int\n\nNotes\n-----\nCall-back functions::\n\n  def cselect(arg): return cselect\n  Required arguments:\n    arg : input complex\n  Return objects:\n    cselect : int\n"
    pass

def cgeev():
    "w,vl,vr,info = cgeev(a,[compute_vl,compute_vr,lwork,overwrite_a])\n\nWrapper for ``cgeev``.\n\nParameters\n----------\na : input rank-2 array('F') with bounds (n,n)\n\nOther Parameters\n----------------\ncompute_vl : input int, optional\n    Default: 1\ncompute_vr : input int, optional\n    Default: 1\noverwrite_a : input int, optional\n    Default: 0\nlwork : input int, optional\n    Default: 2*n\n\nReturns\n-------\nw : rank-1 array('F') with bounds (n)\nvl : rank-2 array('F') with bounds (ldvl,n)\nvr : rank-2 array('F') with bounds (ldvr,n)\ninfo : int\n"
    pass

def cgeev_lwork():
    'work,info = cgeev_lwork(n,[compute_vl,compute_vr])\n\nWrapper for ``cgeev_lwork``.\n\nParameters\n----------\nn : input int\n\nOther Parameters\n----------------\ncompute_vl : input int, optional\n    Default: 1\ncompute_vr : input int, optional\n    Default: 1\n\nReturns\n-------\nwork : complex\ninfo : int\n'
    pass

def cgegv(*args, **kwds):
    "`cgegv` is deprecated!\nThe `*gegv` family of routines has been deprecated in\nLAPACK 3.6.0 in favor of the `*ggev` family of routines.\nThe corresponding wrappers will be removed from SciPy in\na future release.\n\nalpha,beta,vl,vr,info = cgegv(a,b,[compute_vl,compute_vr,lwork,overwrite_a,overwrite_b])\n\nWrapper for ``cgegv``.\n\nParameters\n----------\na : input rank-2 array('F') with bounds (n,n)\nb : input rank-2 array('F') with bounds (n,n)\n\nOther Parameters\n----------------\ncompute_vl : input int, optional\n    Default: 1\ncompute_vr : input int, optional\n    Default: 1\noverwrite_a : input int, optional\n    Default: 0\noverwrite_b : input int, optional\n    Default: 0\nlwork : input int, optional\n    Default: 2*n\n\nReturns\n-------\nalpha : rank-1 array('F') with bounds (n)\nbeta : rank-1 array('F') with bounds (n)\nvl : rank-2 array('F') with bounds (ldvl,n)\nvr : rank-2 array('F') with bounds (ldvr,n)\ninfo : int\n"
    pass

def cgehrd():
    "ht,tau,info = cgehrd(a,[lo,hi,lwork,overwrite_a])\n\nWrapper for ``cgehrd``.\n\nParameters\n----------\na : input rank-2 array('F') with bounds (n,n)\n\nOther Parameters\n----------------\nlo : input int, optional\n    Default: 0\nhi : input int, optional\n    Default: n-1\noverwrite_a : input int, optional\n    Default: 0\nlwork : input int, optional\n    Default: MAX(n,1)\n\nReturns\n-------\nht : rank-2 array('F') with bounds (n,n) and a storage\ntau : rank-1 array('F') with bounds (n - 1)\ninfo : int\n"
    pass

def cgehrd_lwork():
    'work,info = cgehrd_lwork(n,[lo,hi])\n\nWrapper for ``cgehrd_lwork``.\n\nParameters\n----------\nn : input int\n\nOther Parameters\n----------------\nlo : input int, optional\n    Default: 0\nhi : input int, optional\n    Default: n-1\n\nReturns\n-------\nwork : complex\ninfo : int\n'
    pass

def cgelsd():
    "x,s,rank,info = cgelsd(a,b,lwork,size_rwork,size_iwork,[cond,overwrite_a,overwrite_b])\n\nWrapper for ``cgelsd``.\n\nParameters\n----------\na : input rank-2 array('F') with bounds (m,n)\nb : input rank-2 array('F') with bounds (maxmn,nrhs)\nlwork : input int\nsize_rwork : input int\nsize_iwork : input int\n\nOther Parameters\n----------------\noverwrite_a : input int, optional\n    Default: 0\noverwrite_b : input int, optional\n    Default: 0\ncond : input float, optional\n    Default: -1.0\n\nReturns\n-------\nx : rank-2 array('F') with bounds (maxmn,nrhs) and b storage\ns : rank-1 array('f') with bounds (minmn)\nrank : int\ninfo : int\n"
    pass

def cgelsd_lwork():
    'work,rwork,iwork,info = cgelsd_lwork(m,n,nrhs,[cond,lwork])\n\nWrapper for ``cgelsd_lwork``.\n\nParameters\n----------\nm : input int\nn : input int\nnrhs : input int\n\nOther Parameters\n----------------\ncond : input float, optional\n    Default: -1.0\nlwork : input int, optional\n    Default: -1\n\nReturns\n-------\nwork : complex\nrwork : float\niwork : int\ninfo : int\n'
    pass

def cgelss():
    "v,x,s,rank,work,info = cgelss(a,b,[cond,lwork,overwrite_a,overwrite_b])\n\nWrapper for ``cgelss``.\n\nParameters\n----------\na : input rank-2 array('F') with bounds (m,n)\nb : input rank-2 array('F') with bounds (maxmn,nrhs)\n\nOther Parameters\n----------------\noverwrite_a : input int, optional\n    Default: 0\noverwrite_b : input int, optional\n    Default: 0\ncond : input float, optional\n    Default: -1.0\nlwork : input int, optional\n    Default: 2*minmn+MAX(maxmn,nrhs)\n\nReturns\n-------\nv : rank-2 array('F') with bounds (m,n) and a storage\nx : rank-2 array('F') with bounds (maxmn,nrhs) and b storage\ns : rank-1 array('f') with bounds (minmn)\nrank : int\nwork : rank-1 array('F') with bounds (MAX(lwork,1))\ninfo : int\n"
    pass

def cgelss_lwork():
    'work,info = cgelss_lwork(m,n,nrhs,[cond,lwork])\n\nWrapper for ``cgelss_lwork``.\n\nParameters\n----------\nm : input int\nn : input int\nnrhs : input int\n\nOther Parameters\n----------------\ncond : input float, optional\n    Default: -1.0\nlwork : input int, optional\n    Default: -1\n\nReturns\n-------\nwork : complex\ninfo : int\n'
    pass

def cgelsy():
    "v,x,j,rank,info = cgelsy(a,b,jptv,cond,lwork,[overwrite_a,overwrite_b])\n\nWrapper for ``cgelsy``.\n\nParameters\n----------\na : input rank-2 array('F') with bounds (m,n)\nb : input rank-2 array('F') with bounds (maxmn,nrhs)\njptv : input rank-1 array('i') with bounds (n)\ncond : input float\nlwork : input int\n\nOther Parameters\n----------------\noverwrite_a : input int, optional\n    Default: 0\noverwrite_b : input int, optional\n    Default: 0\n\nReturns\n-------\nv : rank-2 array('F') with bounds (m,n) and a storage\nx : rank-2 array('F') with bounds (maxmn,nrhs) and b storage\nj : rank-1 array('i') with bounds (n) and jptv storage\nrank : int\ninfo : int\n"
    pass

def cgelsy_lwork():
    'work,info = cgelsy_lwork(m,n,nrhs,cond,[lwork])\n\nWrapper for ``cgelsy_lwork``.\n\nParameters\n----------\nm : input int\nn : input int\nnrhs : input int\ncond : input float\n\nOther Parameters\n----------------\nlwork : input int, optional\n    Default: -1\n\nReturns\n-------\nwork : complex\ninfo : int\n'
    pass

def cgeqp3():
    "qr,jpvt,tau,work,info = cgeqp3(a,[lwork,overwrite_a])\n\nWrapper for ``cgeqp3``.\n\nParameters\n----------\na : input rank-2 array('F') with bounds (m,n)\n\nOther Parameters\n----------------\noverwrite_a : input int, optional\n    Default: 0\nlwork : input int, optional\n    Default: 3*(n+1)\n\nReturns\n-------\nqr : rank-2 array('F') with bounds (m,n) and a storage\njpvt : rank-1 array('i') with bounds (n)\ntau : rank-1 array('F') with bounds (MIN(m,n))\nwork : rank-1 array('F') with bounds (MAX(lwork,1))\ninfo : int\n"
    pass

def cgeqrf():
    "qr,tau,work,info = cgeqrf(a,[lwork,overwrite_a])\n\nWrapper for ``cgeqrf``.\n\nParameters\n----------\na : input rank-2 array('F') with bounds (m,n)\n\nOther Parameters\n----------------\noverwrite_a : input int, optional\n    Default: 0\nlwork : input int, optional\n    Default: 3*n\n\nReturns\n-------\nqr : rank-2 array('F') with bounds (m,n) and a storage\ntau : rank-1 array('F') with bounds (MIN(m,n))\nwork : rank-1 array('F') with bounds (MAX(lwork,1))\ninfo : int\n"
    pass

def cgerqf():
    "qr,tau,work,info = cgerqf(a,[lwork,overwrite_a])\n\nWrapper for ``cgerqf``.\n\nParameters\n----------\na : input rank-2 array('F') with bounds (m,n)\n\nOther Parameters\n----------------\noverwrite_a : input int, optional\n    Default: 0\nlwork : input int, optional\n    Default: 3*m\n\nReturns\n-------\nqr : rank-2 array('F') with bounds (m,n) and a storage\ntau : rank-1 array('F') with bounds (MIN(m,n))\nwork : rank-1 array('F') with bounds (MAX(lwork,1))\ninfo : int\n"
    pass

def cgesdd():
    "u,s,vt,info = cgesdd(a,[compute_uv,full_matrices,lwork,overwrite_a])\n\nWrapper for ``cgesdd``.\n\nParameters\n----------\na : input rank-2 array('F') with bounds (m,n)\n\nOther Parameters\n----------------\noverwrite_a : input int, optional\n    Default: 0\ncompute_uv : input int, optional\n    Default: 1\nfull_matrices : input int, optional\n    Default: 1\nlwork : input int, optional\n    Default: (compute_uv?2*minmn*minmn+MAX(m,n)+2*minmn:2*minmn+MAX(m,n))\n\nReturns\n-------\nu : rank-2 array('F') with bounds (u0,u1)\ns : rank-1 array('f') with bounds (minmn)\nvt : rank-2 array('F') with bounds (vt0,vt1)\ninfo : int\n"
    pass

def cgesdd_lwork():
    'work,info = cgesdd_lwork(m,n,[compute_uv,full_matrices])\n\nWrapper for ``cgesdd_lwork``.\n\nParameters\n----------\nm : input int\nn : input int\n\nOther Parameters\n----------------\ncompute_uv : input int, optional\n    Default: 1\nfull_matrices : input int, optional\n    Default: 1\n\nReturns\n-------\nwork : complex\ninfo : int\n'
    pass

def cgesv():
    "lu,piv,x,info = cgesv(a,b,[overwrite_a,overwrite_b])\n\nWrapper for ``cgesv``.\n\nParameters\n----------\na : input rank-2 array('F') with bounds (n,n)\nb : input rank-2 array('F') with bounds (n,nrhs)\n\nOther Parameters\n----------------\noverwrite_a : input int, optional\n    Default: 0\noverwrite_b : input int, optional\n    Default: 0\n\nReturns\n-------\nlu : rank-2 array('F') with bounds (n,n) and a storage\npiv : rank-1 array('i') with bounds (n)\nx : rank-2 array('F') with bounds (n,nrhs) and b storage\ninfo : int\n"
    pass

def cgesvd():
    "u,s,vt,info = cgesvd(a,[compute_uv,full_matrices,lwork,overwrite_a])\n\nWrapper for ``cgesvd``.\n\nParameters\n----------\na : input rank-2 array('F') with bounds (m,n)\n\nOther Parameters\n----------------\noverwrite_a : input int, optional\n    Default: 0\ncompute_uv : input int, optional\n    Default: 1\nfull_matrices : input int, optional\n    Default: 1\nlwork : input int, optional\n    Default: MAX(1,2*minmn+MAX(m,n))\n\nReturns\n-------\nu : rank-2 array('F') with bounds (u0,u1)\ns : rank-1 array('f') with bounds (minmn)\nvt : rank-2 array('F') with bounds (vt0,vt1)\ninfo : int\n"
    pass

def cgesvd_lwork():
    'work,info = cgesvd_lwork(m,n,[compute_uv,full_matrices])\n\nWrapper for ``cgesvd_lwork``.\n\nParameters\n----------\nm : input int\nn : input int\n\nOther Parameters\n----------------\ncompute_uv : input int, optional\n    Default: 1\nfull_matrices : input int, optional\n    Default: 1\n\nReturns\n-------\nwork : complex\ninfo : int\n'
    pass

def cgesvx():
    "as,lu,ipiv,equed,rs,cs,bs,x,rcond,ferr,berr,info = cgesvx(a,b,[fact,trans,af,ipiv,equed,r,c,overwrite_a,overwrite_b])\n\nWrapper for ``cgesvx``.\n\nParameters\n----------\na : input rank-2 array('F') with bounds (n,n)\nb : input rank-2 array('F') with bounds (n,nrhs)\n\nOther Parameters\n----------------\nfact : input string(len=1), optional\n    Default: 'E'\ntrans : input string(len=1), optional\n    Default: 'N'\noverwrite_a : input int, optional\n    Default: 0\naf : input rank-2 array('F') with bounds (n,n)\nipiv : input rank-1 array('i') with bounds (n)\nequed : input string(len=1), optional\n    Default: 'B'\nr : input rank-1 array('f') with bounds (n)\nc : input rank-1 array('f') with bounds (n)\noverwrite_b : input int, optional\n    Default: 0\n\nReturns\n-------\nas : rank-2 array('F') with bounds (n,n) and a storage\nlu : rank-2 array('F') with bounds (n,n) and af storage\nipiv : rank-1 array('i') with bounds (n)\nequed : string(len=1)\nrs : rank-1 array('f') with bounds (n) and r storage\ncs : rank-1 array('f') with bounds (n) and c storage\nbs : rank-2 array('F') with bounds (n,nrhs) and b storage\nx : rank-2 array('F') with bounds (n,nrhs)\nrcond : float\nferr : rank-1 array('f') with bounds (nrhs)\nberr : rank-1 array('f') with bounds (nrhs)\ninfo : int\n"
    pass

def cgetrf():
    "lu,piv,info = cgetrf(a,[overwrite_a])\n\nWrapper for ``cgetrf``.\n\nParameters\n----------\na : input rank-2 array('F') with bounds (m,n)\n\nOther Parameters\n----------------\noverwrite_a : input int, optional\n    Default: 0\n\nReturns\n-------\nlu : rank-2 array('F') with bounds (m,n) and a storage\npiv : rank-1 array('i') with bounds (MIN(m,n))\ninfo : int\n"
    pass

def cgetri():
    "inv_a,info = cgetri(lu,piv,[lwork,overwrite_lu])\n\nWrapper for ``cgetri``.\n\nParameters\n----------\nlu : input rank-2 array('F') with bounds (n,n)\npiv : input rank-1 array('i') with bounds (n)\n\nOther Parameters\n----------------\noverwrite_lu : input int, optional\n    Default: 0\nlwork : input int, optional\n    Default: 3*n\n\nReturns\n-------\ninv_a : rank-2 array('F') with bounds (n,n) and lu storage\ninfo : int\n"
    pass

def cgetri_lwork():
    'work,info = cgetri_lwork(n)\n\nWrapper for ``cgetri_lwork``.\n\nParameters\n----------\nn : input int\n\nReturns\n-------\nwork : complex\ninfo : int\n'
    pass

def cgetrs():
    "x,info = cgetrs(lu,piv,b,[trans,overwrite_b])\n\nWrapper for ``cgetrs``.\n\nParameters\n----------\nlu : input rank-2 array('F') with bounds (n,n)\npiv : input rank-1 array('i') with bounds (n)\nb : input rank-2 array('F') with bounds (n,nrhs)\n\nOther Parameters\n----------------\noverwrite_b : input int, optional\n    Default: 0\ntrans : input int, optional\n    Default: 0\n\nReturns\n-------\nx : rank-2 array('F') with bounds (n,nrhs) and b storage\ninfo : int\n"
    pass

def cgges():
    "a,b,sdim,alpha,beta,vsl,vsr,work,info = cgges(cselect,a,b,[jobvsl,jobvsr,sort_t,ldvsl,ldvsr,lwork,cselect_extra_args,overwrite_a,overwrite_b])\n\nWrapper for ``cgges``.\n\nParameters\n----------\ncselect : call-back function\na : input rank-2 array('F') with bounds (lda,n)\nb : input rank-2 array('F') with bounds (ldb,n)\n\nOther Parameters\n----------------\njobvsl : input int, optional\n    Default: 1\njobvsr : input int, optional\n    Default: 1\nsort_t : input int, optional\n    Default: 0\ncselect_extra_args : input tuple, optional\n    Default: ()\noverwrite_a : input int, optional\n    Default: 0\noverwrite_b : input int, optional\n    Default: 0\nldvsl : input int, optional\n    Default: ((jobvsl==1)?n:1)\nldvsr : input int, optional\n    Default: ((jobvsr==1)?n:1)\nlwork : input int, optional\n    Default: 2*n\n\nReturns\n-------\na : rank-2 array('F') with bounds (lda,n)\nb : rank-2 array('F') with bounds (ldb,n)\nsdim : int\nalpha : rank-1 array('F') with bounds (n)\nbeta : rank-1 array('F') with bounds (n)\nvsl : rank-2 array('F') with bounds (ldvsl,n)\nvsr : rank-2 array('F') with bounds (ldvsr,n)\nwork : rank-1 array('F') with bounds (MAX(lwork,1))\ninfo : int\n\nNotes\n-----\nCall-back functions::\n\n  def cselect(alpha,beta): return cselect\n  Required arguments:\n    alpha : input complex\n    beta : input complex\n  Return objects:\n    cselect : int\n"
    pass

def cggev():
    "alpha,beta,vl,vr,work,info = cggev(a,b,[compute_vl,compute_vr,lwork,overwrite_a,overwrite_b])\n\nWrapper for ``cggev``.\n\nParameters\n----------\na : input rank-2 array('F') with bounds (n,n)\nb : input rank-2 array('F') with bounds (n,n)\n\nOther Parameters\n----------------\ncompute_vl : input int, optional\n    Default: 1\ncompute_vr : input int, optional\n    Default: 1\noverwrite_a : input int, optional\n    Default: 0\noverwrite_b : input int, optional\n    Default: 0\nlwork : input int, optional\n    Default: 2*n\n\nReturns\n-------\nalpha : rank-1 array('F') with bounds (n)\nbeta : rank-1 array('F') with bounds (n)\nvl : rank-2 array('F') with bounds (ldvl,n)\nvr : rank-2 array('F') with bounds (ldvr,n)\nwork : rank-1 array('F') with bounds (MAX(lwork,1))\ninfo : int\n"
    pass

def cgtsv():
    "du2,d,du,x,info = cgtsv(dl,d,du,b,[overwrite_dl,overwrite_d,overwrite_du,overwrite_b])\n\nWrapper for ``cgtsv``.\n\nParameters\n----------\ndl : input rank-1 array('F') with bounds (n - 1)\nd : input rank-1 array('F') with bounds (n)\ndu : input rank-1 array('F') with bounds (n - 1)\nb : input rank-2 array('F') with bounds (n,nrhs)\n\nOther Parameters\n----------------\noverwrite_dl : input int, optional\n    Default: 0\noverwrite_d : input int, optional\n    Default: 0\noverwrite_du : input int, optional\n    Default: 0\noverwrite_b : input int, optional\n    Default: 0\n\nReturns\n-------\ndu2 : rank-1 array('F') with bounds (n - 1) and dl storage\nd : rank-1 array('F') with bounds (n)\ndu : rank-1 array('F') with bounds (n - 1)\nx : rank-2 array('F') with bounds (n,nrhs) and b storage\ninfo : int\n"
    pass

def chbevd():
    "w,z,info = chbevd(ab,[compute_v,lower,ldab,lrwork,liwork,overwrite_ab])\n\nWrapper for ``chbevd``.\n\nParameters\n----------\nab : input rank-2 array('F') with bounds (ldab,n)\n\nOther Parameters\n----------------\noverwrite_ab : input int, optional\n    Default: 1\ncompute_v : input int, optional\n    Default: 1\nlower : input int, optional\n    Default: 0\nldab : input int, optional\n    Default: shape(ab,0)\nlrwork : input int, optional\n    Default: (compute_v?1+5*n+2*n*n:n)\nliwork : input int, optional\n    Default: (compute_v?3+5*n:1)\n\nReturns\n-------\nw : rank-1 array('f') with bounds (n)\nz : rank-2 array('F') with bounds (ldz,ldz)\ninfo : int\n"
    pass

def chbevx():
    "w,z,m,ifail,info = chbevx(ab,vl,vu,il,iu,[ldab,compute_v,range,lower,abstol,mmax,overwrite_ab])\n\nWrapper for ``chbevx``.\n\nParameters\n----------\nab : input rank-2 array('F') with bounds (ldab,n)\nvl : input float\nvu : input float\nil : input int\niu : input int\n\nOther Parameters\n----------------\noverwrite_ab : input int, optional\n    Default: 1\nldab : input int, optional\n    Default: shape(ab,0)\ncompute_v : input int, optional\n    Default: 1\nrange : input int, optional\n    Default: 0\nlower : input int, optional\n    Default: 0\nabstol : input float, optional\n    Default: 0.0\nmmax : input int, optional\n    Default: (compute_v?(range==2?(iu-il+1):n):1)\n\nReturns\n-------\nw : rank-1 array('f') with bounds (n)\nz : rank-2 array('F') with bounds (ldz,mmax)\nm : int\nifail : rank-1 array('i') with bounds ((compute_v?n:1))\ninfo : int\n"
    pass

def cheev():
    "w,v,info = cheev(a,[compute_v,lower,lwork,overwrite_a])\n\nWrapper for ``cheev``.\n\nParameters\n----------\na : input rank-2 array('F') with bounds (n,n)\n\nOther Parameters\n----------------\ncompute_v : input int, optional\n    Default: 1\nlower : input int, optional\n    Default: 0\noverwrite_a : input int, optional\n    Default: 0\nlwork : input int, optional\n    Default: 2*n-1\n\nReturns\n-------\nw : rank-1 array('f') with bounds (n)\nv : rank-2 array('F') with bounds (n,n) and a storage\ninfo : int\n"
    pass

def cheevd():
    "w,v,info = cheevd(a,[compute_v,lower,lwork,overwrite_a])\n\nWrapper for ``cheevd``.\n\nParameters\n----------\na : input rank-2 array('F') with bounds (n,n)\n\nOther Parameters\n----------------\ncompute_v : input int, optional\n    Default: 1\nlower : input int, optional\n    Default: 0\noverwrite_a : input int, optional\n    Default: 0\nlwork : input int, optional\n    Default: (compute_v?2*n+n*n:n+1)\n\nReturns\n-------\nw : rank-1 array('f') with bounds (n)\nv : rank-2 array('F') with bounds (n,n) and a storage\ninfo : int\n"
    pass

def cheevr():
    "w,z,info = cheevr(a,[jobz,range,uplo,il,iu,lwork,overwrite_a])\n\nWrapper for ``cheevr``.\n\nParameters\n----------\na : input rank-2 array('F') with bounds (n,n)\n\nOther Parameters\n----------------\njobz : input string(len=1), optional\n    Default: 'V'\nrange : input string(len=1), optional\n    Default: 'A'\nuplo : input string(len=1), optional\n    Default: 'L'\noverwrite_a : input int, optional\n    Default: 0\nil : input int, optional\n    Default: 1\niu : input int, optional\n    Default: n\nlwork : input int, optional\n    Default: 18*n\n\nReturns\n-------\nw : rank-1 array('f') with bounds (n)\nz : rank-2 array('F') with bounds (n,m)\ninfo : int\n"
    pass

def chegv():
    "a,w,info = chegv(a,b,[itype,jobz,uplo,overwrite_a,overwrite_b])\n\nWrapper for ``chegv``.\n\nParameters\n----------\na : input rank-2 array('F') with bounds (n,n)\nb : input rank-2 array('F') with bounds (n,n)\n\nOther Parameters\n----------------\nitype : input int, optional\n    Default: 1\njobz : input string(len=1), optional\n    Default: 'V'\nuplo : input string(len=1), optional\n    Default: 'L'\noverwrite_a : input int, optional\n    Default: 0\noverwrite_b : input int, optional\n    Default: 0\n\nReturns\n-------\na : rank-2 array('F') with bounds (n,n)\nw : rank-1 array('f') with bounds (n)\ninfo : int\n"
    pass

def chegvd():
    "a,w,info = chegvd(a,b,[itype,jobz,uplo,lwork,overwrite_a,overwrite_b])\n\nWrapper for ``chegvd``.\n\nParameters\n----------\na : input rank-2 array('F') with bounds (n,n)\nb : input rank-2 array('F') with bounds (n,n)\n\nOther Parameters\n----------------\nitype : input int, optional\n    Default: 1\njobz : input string(len=1), optional\n    Default: 'V'\nuplo : input string(len=1), optional\n    Default: 'L'\noverwrite_a : input int, optional\n    Default: 0\noverwrite_b : input int, optional\n    Default: 0\nlwork : input int, optional\n    Default: 2*n+n*n\n\nReturns\n-------\na : rank-2 array('F') with bounds (n,n)\nw : rank-1 array('f') with bounds (n)\ninfo : int\n"
    pass

def chegvx():
    "w,z,ifail,info = chegvx(a,b,iu,[itype,jobz,uplo,il,lwork,overwrite_a,overwrite_b])\n\nWrapper for ``chegvx``.\n\nParameters\n----------\na : input rank-2 array('F') with bounds (n,n)\nb : input rank-2 array('F') with bounds (n,n)\niu : input int\n\nOther Parameters\n----------------\nitype : input int, optional\n    Default: 1\njobz : input string(len=1), optional\n    Default: 'V'\nuplo : input string(len=1), optional\n    Default: 'L'\noverwrite_a : input int, optional\n    Default: 0\noverwrite_b : input int, optional\n    Default: 0\nil : input int, optional\n    Default: 1\nlwork : input int, optional\n    Default: 18*n-1\n\nReturns\n-------\nw : rank-1 array('f') with bounds (n)\nz : rank-2 array('F') with bounds (n,m)\nifail : rank-1 array('i') with bounds (n)\ninfo : int\n"
    pass

def chesv():
    "uduh,ipiv,x,info = chesv(a,b,[lwork,lower,overwrite_a,overwrite_b])\n\nWrapper for ``chesv``.\n\nParameters\n----------\na : input rank-2 array('F') with bounds (n,n)\nb : input rank-2 array('F') with bounds (n,nrhs)\n\nOther Parameters\n----------------\noverwrite_a : input int, optional\n    Default: 0\noverwrite_b : input int, optional\n    Default: 0\nlwork : input int, optional\n    Default: n\nlower : input int, optional\n    Default: 0\n\nReturns\n-------\nuduh : rank-2 array('F') with bounds (n,n) and a storage\nipiv : rank-1 array('i') with bounds (n)\nx : rank-2 array('F') with bounds (n,nrhs) and b storage\ninfo : int\n"
    pass

def chesv_lwork():
    'work,info = chesv_lwork(n,[lower])\n\nWrapper for ``chesv_lwork``.\n\nParameters\n----------\nn : input int\n\nOther Parameters\n----------------\nlower : input int, optional\n    Default: 0\n\nReturns\n-------\nwork : complex\ninfo : int\n'
    pass

def chesvx():
    "uduh,ipiv,x,rcond,ferr,berr,info = chesvx(a,b,[af,ipiv,lwork,factored,lower,overwrite_a,overwrite_b])\n\nWrapper for ``chesvx``.\n\nParameters\n----------\na : input rank-2 array('F') with bounds (n,n)\nb : input rank-2 array('F') with bounds (n,nrhs)\n\nOther Parameters\n----------------\noverwrite_a : input int, optional\n    Default: 0\naf : input rank-2 array('F') with bounds (n,n)\nipiv : input rank-1 array('i') with bounds (n)\noverwrite_b : input int, optional\n    Default: 0\nlwork : input int, optional\n    Default: 2*n\nfactored : input int, optional\n    Default: 0\nlower : input int, optional\n    Default: 0\n\nReturns\n-------\nuduh : rank-2 array('F') with bounds (n,n) and af storage\nipiv : rank-1 array('i') with bounds (n)\nx : rank-2 array('F') with bounds (n,nrhs)\nrcond : float\nferr : rank-1 array('f') with bounds (nrhs)\nberr : rank-1 array('f') with bounds (nrhs)\ninfo : int\n"
    pass

def chesvx_lwork():
    'work,info = chesvx_lwork(n,[lower])\n\nWrapper for ``chesvx_lwork``.\n\nParameters\n----------\nn : input int\n\nOther Parameters\n----------------\nlower : input int, optional\n    Default: 0\n\nReturns\n-------\nwork : complex\ninfo : int\n'
    pass

def clange():
    "n2 = clange(norm,a)\n\nWrapper for ``clange``.\n\nParameters\n----------\nnorm : input string(len=1)\na : input rank-2 array('F') with bounds (m,n)\n\nReturns\n-------\nn2 : float\n"
    pass

def clarf():
    "c = clarf(v,tau,c,work,[side,incv,overwrite_c])\n\nWrapper for ``clarf``.\n\nParameters\n----------\nv : input rank-1 array('F') with bounds (*)\ntau : input complex\nc : input rank-2 array('F') with bounds (m,n)\nwork : input rank-1 array('F') with bounds (*)\n\nOther Parameters\n----------------\nside : input string(len=1), optional\n    Default: 'L'\nincv : input int, optional\n    Default: 1\noverwrite_c : input int, optional\n    Default: 0\n\nReturns\n-------\nc : rank-2 array('F') with bounds (m,n)\n"
    pass

def clarfg():
    "alpha,x,tau = clarfg(n,alpha,x,[incx,overwrite_x])\n\nWrapper for ``clarfg``.\n\nParameters\n----------\nn : input int\nalpha : input complex\nx : input rank-1 array('F') with bounds (*)\n\nOther Parameters\n----------------\noverwrite_x : input int, optional\n    Default: 0\nincx : input int, optional\n    Default: 1\n\nReturns\n-------\nalpha : complex\nx : rank-1 array('F') with bounds (*)\ntau : complex\n"
    pass

def clartg():
    'cs,sn,r = clartg(f,g)\n\nWrapper for ``clartg``.\n\nParameters\n----------\nf : input complex\ng : input complex\n\nReturns\n-------\ncs : float\nsn : complex\nr : complex\n'
    pass

def claswp():
    "a = claswp(a,piv,[k1,k2,off,inc,overwrite_a])\n\nWrapper for ``claswp``.\n\nParameters\n----------\na : input rank-2 array('F') with bounds (nrows,n)\npiv : input rank-1 array('i') with bounds (*)\n\nOther Parameters\n----------------\noverwrite_a : input int, optional\n    Default: 0\nk1 : input int, optional\n    Default: 0\nk2 : input int, optional\n    Default: len(piv)-1\noff : input int, optional\n    Default: 0\ninc : input int, optional\n    Default: 1\n\nReturns\n-------\na : rank-2 array('F') with bounds (nrows,n)\n"
    pass

def clauum():
    "a,info = clauum(c,[lower,overwrite_c])\n\nWrapper for ``clauum``.\n\nParameters\n----------\nc : input rank-2 array('F') with bounds (n,n)\n\nOther Parameters\n----------------\noverwrite_c : input int, optional\n    Default: 0\nlower : input int, optional\n    Default: 0\n\nReturns\n-------\na : rank-2 array('F') with bounds (n,n) and c storage\ninfo : int\n"
    pass

def cpbsv():
    "c,x,info = cpbsv(ab,b,[lower,ldab,overwrite_ab,overwrite_b])\n\nWrapper for ``cpbsv``.\n\nParameters\n----------\nab : input rank-2 array('F') with bounds (ldab,n)\nb : input rank-2 array('F') with bounds (ldb,nrhs)\n\nOther Parameters\n----------------\nlower : input int, optional\n    Default: 0\noverwrite_ab : input int, optional\n    Default: 0\nldab : input int, optional\n    Default: shape(ab,0)\noverwrite_b : input int, optional\n    Default: 0\n\nReturns\n-------\nc : rank-2 array('F') with bounds (ldab,n) and ab storage\nx : rank-2 array('F') with bounds (ldb,nrhs) and b storage\ninfo : int\n"
    pass

def cpbtrf():
    "c,info = cpbtrf(ab,[lower,ldab,overwrite_ab])\n\nWrapper for ``cpbtrf``.\n\nParameters\n----------\nab : input rank-2 array('F') with bounds (ldab,n)\n\nOther Parameters\n----------------\nlower : input int, optional\n    Default: 0\noverwrite_ab : input int, optional\n    Default: 0\nldab : input int, optional\n    Default: shape(ab,0)\n\nReturns\n-------\nc : rank-2 array('F') with bounds (ldab,n) and ab storage\ninfo : int\n"
    pass

def cpbtrs():
    "x,info = cpbtrs(ab,b,[lower,ldab,overwrite_b])\n\nWrapper for ``cpbtrs``.\n\nParameters\n----------\nab : input rank-2 array('F') with bounds (ldab,n)\nb : input rank-2 array('F') with bounds (ldb,nrhs)\n\nOther Parameters\n----------------\nlower : input int, optional\n    Default: 0\nldab : input int, optional\n    Default: shape(ab,0)\noverwrite_b : input int, optional\n    Default: 0\n\nReturns\n-------\nx : rank-2 array('F') with bounds (ldb,nrhs) and b storage\ninfo : int\n"
    pass

def cpocon():
    "rcond,info = cpocon(a,anorm,[uplo])\n\nWrapper for ``cpocon``.\n\nParameters\n----------\na : input rank-2 array('F') with bounds (n,n)\nanorm : input float\n\nOther Parameters\n----------------\nuplo : input string(len=1), optional\n    Default: 'U'\n\nReturns\n-------\nrcond : float\ninfo : int\n"
    pass

def cposv():
    "c,x,info = cposv(a,b,[lower,overwrite_a,overwrite_b])\n\nWrapper for ``cposv``.\n\nParameters\n----------\na : input rank-2 array('F') with bounds (n,n)\nb : input rank-2 array('F') with bounds (n,nrhs)\n\nOther Parameters\n----------------\noverwrite_a : input int, optional\n    Default: 0\noverwrite_b : input int, optional\n    Default: 0\nlower : input int, optional\n    Default: 0\n\nReturns\n-------\nc : rank-2 array('F') with bounds (n,n) and a storage\nx : rank-2 array('F') with bounds (n,nrhs) and b storage\ninfo : int\n"
    pass

def cposvx():
    "a_s,lu,equed,s,b_s,x,rcond,ferr,berr,info = cposvx(a,b,[fact,af,equed,s,lower,overwrite_a,overwrite_b])\n\nWrapper for ``cposvx``.\n\nParameters\n----------\na : input rank-2 array('F') with bounds (n,n)\nb : input rank-2 array('F') with bounds (n,nrhs)\n\nOther Parameters\n----------------\nfact : input string(len=1), optional\n    Default: 'E'\noverwrite_a : input int, optional\n    Default: 0\naf : input rank-2 array('F') with bounds (n,n)\nequed : input string(len=1), optional\n    Default: 'Y'\ns : input rank-1 array('f') with bounds (n)\noverwrite_b : input int, optional\n    Default: 0\nlower : input int, optional\n    Default: 0\n\nReturns\n-------\na_s : rank-2 array('F') with bounds (n,n) and a storage\nlu : rank-2 array('F') with bounds (n,n) and af storage\nequed : string(len=1)\ns : rank-1 array('f') with bounds (n)\nb_s : rank-2 array('F') with bounds (n,nrhs) and b storage\nx : rank-2 array('F') with bounds (n,nrhs)\nrcond : float\nferr : rank-1 array('f') with bounds (nrhs)\nberr : rank-1 array('f') with bounds (nrhs)\ninfo : int\n"
    pass

def cpotrf():
    "c,info = cpotrf(a,[lower,clean,overwrite_a])\n\nWrapper for ``cpotrf``.\n\nParameters\n----------\na : input rank-2 array('F') with bounds (n,n)\n\nOther Parameters\n----------------\noverwrite_a : input int, optional\n    Default: 0\nlower : input int, optional\n    Default: 0\nclean : input int, optional\n    Default: 1\n\nReturns\n-------\nc : rank-2 array('F') with bounds (n,n) and a storage\ninfo : int\n"
    pass

def cpotri():
    "inv_a,info = cpotri(c,[lower,overwrite_c])\n\nWrapper for ``cpotri``.\n\nParameters\n----------\nc : input rank-2 array('F') with bounds (n,n)\n\nOther Parameters\n----------------\noverwrite_c : input int, optional\n    Default: 0\nlower : input int, optional\n    Default: 0\n\nReturns\n-------\ninv_a : rank-2 array('F') with bounds (n,n) and c storage\ninfo : int\n"
    pass

def cpotrs():
    "x,info = cpotrs(c,b,[lower,overwrite_b])\n\nWrapper for ``cpotrs``.\n\nParameters\n----------\nc : input rank-2 array('F') with bounds (n,n)\nb : input rank-2 array('F') with bounds (n,nrhs)\n\nOther Parameters\n----------------\noverwrite_b : input int, optional\n    Default: 0\nlower : input int, optional\n    Default: 0\n\nReturns\n-------\nx : rank-2 array('F') with bounds (n,nrhs) and b storage\ninfo : int\n"
    pass

def cptsv():
    "d,du,x,info = cptsv(d,e,b,[overwrite_d,overwrite_e,overwrite_b])\n\nWrapper for ``cptsv``.\n\nParameters\n----------\nd : input rank-1 array('f') with bounds (n)\ne : input rank-1 array('F') with bounds (n - 1)\nb : input rank-2 array('F') with bounds (n,nrhs)\n\nOther Parameters\n----------------\noverwrite_d : input int, optional\n    Default: 0\noverwrite_e : input int, optional\n    Default: 0\noverwrite_b : input int, optional\n    Default: 0\n\nReturns\n-------\nd : rank-1 array('f') with bounds (n)\ndu : rank-1 array('F') with bounds (n - 1) and e storage\nx : rank-2 array('F') with bounds (n,nrhs) and b storage\ninfo : int\n"
    pass

def crot():
    "x,y = crot(x,y,c,s,[n,offx,incx,offy,incy,overwrite_x,overwrite_y])\n\nWrapper for ``crot``.\n\nParameters\n----------\nx : input rank-1 array('F') with bounds (*)\ny : input rank-1 array('F') with bounds (*)\nc : input float\ns : input complex\n\nOther Parameters\n----------------\nn : input int, optional\n    Default: (len(x)-1-offx)/abs(incx)+1\noverwrite_x : input int, optional\n    Default: 0\noffx : input int, optional\n    Default: 0\nincx : input int, optional\n    Default: 1\noverwrite_y : input int, optional\n    Default: 0\noffy : input int, optional\n    Default: 0\nincy : input int, optional\n    Default: 1\n\nReturns\n-------\nx : rank-1 array('F') with bounds (*)\ny : rank-1 array('F') with bounds (*)\n"
    pass

def csysv():
    "udut,ipiv,x,info = csysv(a,b,[lwork,lower,overwrite_a,overwrite_b])\n\nWrapper for ``csysv``.\n\nParameters\n----------\na : input rank-2 array('F') with bounds (n,n)\nb : input rank-2 array('F') with bounds (n,nrhs)\n\nOther Parameters\n----------------\noverwrite_a : input int, optional\n    Default: 0\noverwrite_b : input int, optional\n    Default: 0\nlwork : input int, optional\n    Default: n\nlower : input int, optional\n    Default: 0\n\nReturns\n-------\nudut : rank-2 array('F') with bounds (n,n) and a storage\nipiv : rank-1 array('i') with bounds (n)\nx : rank-2 array('F') with bounds (n,nrhs) and b storage\ninfo : int\n"
    pass

def csysv_lwork():
    'work,info = csysv_lwork(n,[lower])\n\nWrapper for ``csysv_lwork``.\n\nParameters\n----------\nn : input int\n\nOther Parameters\n----------------\nlower : input int, optional\n    Default: 0\n\nReturns\n-------\nwork : complex\ninfo : int\n'
    pass

def csysvx():
    "a_s,udut,ipiv,b_s,x,rcond,ferr,berr,info = csysvx(a,b,[af,ipiv,lwork,factored,lower,overwrite_a,overwrite_b])\n\nWrapper for ``csysvx``.\n\nParameters\n----------\na : input rank-2 array('F') with bounds (n,n)\nb : input rank-2 array('F') with bounds (n,nrhs)\n\nOther Parameters\n----------------\noverwrite_a : input int, optional\n    Default: 0\naf : input rank-2 array('F') with bounds (n,n)\nipiv : input rank-1 array('i') with bounds (n)\noverwrite_b : input int, optional\n    Default: 0\nlwork : input int, optional\n    Default: 3*n\nfactored : input int, optional\n    Default: 0\nlower : input int, optional\n    Default: 0\n\nReturns\n-------\na_s : rank-2 array('F') with bounds (n,n) and a storage\nudut : rank-2 array('F') with bounds (n,n) and af storage\nipiv : rank-1 array('i') with bounds (n)\nb_s : rank-2 array('F') with bounds (n,nrhs) and b storage\nx : rank-2 array('F') with bounds (n,nrhs)\nrcond : float\nferr : rank-1 array('f') with bounds (nrhs)\nberr : rank-1 array('f') with bounds (nrhs)\ninfo : int\n"
    pass

def csysvx_lwork():
    'work,info = csysvx_lwork(n,[lower])\n\nWrapper for ``csysvx_lwork``.\n\nParameters\n----------\nn : input int\n\nOther Parameters\n----------------\nlower : input int, optional\n    Default: 0\n\nReturns\n-------\nwork : complex\ninfo : int\n'
    pass

def ctgsen():
    "a,b,alpha,beta,q,z,m,pl,pr,dif,work,iwork,info = ctgsen(select,a,b,q,z,[lwork,liwork,overwrite_a,overwrite_b,overwrite_q,overwrite_z])\n\nWrapper for ``ctgsen``.\n\nParameters\n----------\nselect : input rank-1 array('i') with bounds (n)\na : input rank-2 array('F') with bounds (lda,n)\nb : input rank-2 array('F') with bounds (ldb,n)\nq : input rank-2 array('F') with bounds (ldq,n)\nz : input rank-2 array('F') with bounds (ldz,n)\n\nOther Parameters\n----------------\noverwrite_a : input int, optional\n    Default: 0\noverwrite_b : input int, optional\n    Default: 0\noverwrite_q : input int, optional\n    Default: 0\noverwrite_z : input int, optional\n    Default: 0\nlwork : input int, optional\n    Default: 2*m*(n-m)\nliwork : input int, optional\n    Default: n+2\n\nReturns\n-------\na : rank-2 array('F') with bounds (lda,n)\nb : rank-2 array('F') with bounds (ldb,n)\nalpha : rank-1 array('F') with bounds (n)\nbeta : rank-1 array('F') with bounds (n)\nq : rank-2 array('F') with bounds (ldq,n)\nz : rank-2 array('F') with bounds (ldz,n)\nm : int\npl : float\npr : float\ndif : rank-1 array('f') with bounds (2)\nwork : rank-1 array('F') with bounds (MAX(lwork,1))\niwork : rank-1 array('i') with bounds (MAX(1,liwork))\ninfo : int\n"
    pass

def ctrsyl():
    "x,scale,info = ctrsyl(a,b,c,[trana,tranb,isgn,overwrite_c])\n\nWrapper for ``ctrsyl``.\n\nParameters\n----------\na : input rank-2 array('F') with bounds (m,m)\nb : input rank-2 array('F') with bounds (n,n)\nc : input rank-2 array('F') with bounds (m,n)\n\nOther Parameters\n----------------\ntrana : input string(len=1), optional\n    Default: 'N'\ntranb : input string(len=1), optional\n    Default: 'N'\nisgn : input int, optional\n    Default: 1\noverwrite_c : input int, optional\n    Default: 0\n\nReturns\n-------\nx : rank-2 array('F') with bounds (m,n) and c storage\nscale : float\ninfo : int\n"
    pass

def ctrtri():
    "inv_c,info = ctrtri(c,[lower,unitdiag,overwrite_c])\n\nWrapper for ``ctrtri``.\n\nParameters\n----------\nc : input rank-2 array('F') with bounds (n,n)\n\nOther Parameters\n----------------\noverwrite_c : input int, optional\n    Default: 0\nlower : input int, optional\n    Default: 0\nunitdiag : input int, optional\n    Default: 0\n\nReturns\n-------\ninv_c : rank-2 array('F') with bounds (n,n) and c storage\ninfo : int\n"
    pass

def ctrtrs():
    "x,info = ctrtrs(a,b,[lower,trans,unitdiag,lda,overwrite_b])\n\nWrapper for ``ctrtrs``.\n\nParameters\n----------\na : input rank-2 array('F') with bounds (lda,n)\nb : input rank-2 array('F') with bounds (ldb,nrhs)\n\nOther Parameters\n----------------\nlower : input int, optional\n    Default: 0\ntrans : input int, optional\n    Default: 0\nunitdiag : input int, optional\n    Default: 0\nlda : input int, optional\n    Default: shape(a,0)\noverwrite_b : input int, optional\n    Default: 0\n\nReturns\n-------\nx : rank-2 array('F') with bounds (ldb,nrhs) and b storage\ninfo : int\n"
    pass

def cunghr():
    "ht,info = cunghr(a,tau,[lo,hi,lwork,overwrite_a])\n\nWrapper for ``cunghr``.\n\nParameters\n----------\na : input rank-2 array('F') with bounds (n,n)\ntau : input rank-1 array('F') with bounds (n - 1)\n\nOther Parameters\n----------------\nlo : input int, optional\n    Default: 0\nhi : input int, optional\n    Default: n-1\noverwrite_a : input int, optional\n    Default: 0\nlwork : input int, optional\n    Default: hi-lo\n\nReturns\n-------\nht : rank-2 array('F') with bounds (n,n) and a storage\ninfo : int\n"
    pass

def cunghr_lwork():
    'work,info = cunghr_lwork(n,[lo,hi])\n\nWrapper for ``cunghr_lwork``.\n\nParameters\n----------\nn : input int\n\nOther Parameters\n----------------\nlo : input int, optional\n    Default: 0\nhi : input int, optional\n    Default: n-1\n\nReturns\n-------\nwork : complex\ninfo : int\n'
    pass

def cungqr():
    "q,work,info = cungqr(a,tau,[lwork,overwrite_a])\n\nWrapper for ``cungqr``.\n\nParameters\n----------\na : input rank-2 array('F') with bounds (m,n)\ntau : input rank-1 array('F') with bounds (k)\n\nOther Parameters\n----------------\noverwrite_a : input int, optional\n    Default: 0\nlwork : input int, optional\n    Default: 3*n\n\nReturns\n-------\nq : rank-2 array('F') with bounds (m,n) and a storage\nwork : rank-1 array('F') with bounds (MAX(lwork,1))\ninfo : int\n"
    pass

def cungrq():
    "q,work,info = cungrq(a,tau,[lwork,overwrite_a])\n\nWrapper for ``cungrq``.\n\nParameters\n----------\na : input rank-2 array('F') with bounds (m,n)\ntau : input rank-1 array('F') with bounds (k)\n\nOther Parameters\n----------------\noverwrite_a : input int, optional\n    Default: 0\nlwork : input int, optional\n    Default: 3*m\n\nReturns\n-------\nq : rank-2 array('F') with bounds (m,n) and a storage\nwork : rank-1 array('F') with bounds (MAX(lwork,1))\ninfo : int\n"
    pass

def cunmqr():
    "cq,work,info = cunmqr(side,trans,a,tau,c,lwork,[overwrite_c])\n\nWrapper for ``cunmqr``.\n\nParameters\n----------\nside : input string(len=1)\ntrans : input string(len=1)\na : input rank-2 array('F') with bounds (lda,k)\ntau : input rank-1 array('F') with bounds (k)\nc : input rank-2 array('F') with bounds (ldc,n)\nlwork : input int\n\nOther Parameters\n----------------\noverwrite_c : input int, optional\n    Default: 0\n\nReturns\n-------\ncq : rank-2 array('F') with bounds (ldc,n) and c storage\nwork : rank-1 array('F') with bounds (MAX(lwork,1))\ninfo : int\n"
    pass

def dgbsv():
    "lub,piv,x,info = dgbsv(kl,ku,ab,b,[overwrite_ab,overwrite_b])\n\nWrapper for ``dgbsv``.\n\nParameters\n----------\nkl : input int\nku : input int\nab : input rank-2 array('d') with bounds (2*kl+ku+1,n)\nb : input rank-2 array('d') with bounds (n,nrhs)\n\nOther Parameters\n----------------\noverwrite_ab : input int, optional\n    Default: 0\noverwrite_b : input int, optional\n    Default: 0\n\nReturns\n-------\nlub : rank-2 array('d') with bounds (2*kl+ku+1,n) and ab storage\npiv : rank-1 array('i') with bounds (n)\nx : rank-2 array('d') with bounds (n,nrhs) and b storage\ninfo : int\n"
    pass

def dgbtrf():
    "lu,ipiv,info = dgbtrf(ab,kl,ku,[m,n,ldab,overwrite_ab])\n\nWrapper for ``dgbtrf``.\n\nParameters\n----------\nab : input rank-2 array('d') with bounds (ldab,*)\nkl : input int\nku : input int\n\nOther Parameters\n----------------\nm : input int, optional\n    Default: shape(ab,1)\nn : input int, optional\n    Default: shape(ab,1)\noverwrite_ab : input int, optional\n    Default: 0\nldab : input int, optional\n    Default: shape(ab,0)\n\nReturns\n-------\nlu : rank-2 array('d') with bounds (ldab,*) and ab storage\nipiv : rank-1 array('i') with bounds (MIN(m,n))\ninfo : int\n"
    pass

def dgbtrs():
    "x,info = dgbtrs(ab,kl,ku,b,ipiv,[trans,n,ldab,ldb,overwrite_b])\n\nWrapper for ``dgbtrs``.\n\nParameters\n----------\nab : input rank-2 array('d') with bounds (ldab,n)\nkl : input int\nku : input int\nb : input rank-2 array('d') with bounds (ldb,nrhs)\nipiv : input rank-1 array('i') with bounds (n)\n\nOther Parameters\n----------------\noverwrite_b : input int, optional\n    Default: 0\ntrans : input int, optional\n    Default: 0\nn : input int, optional\n    Default: shape(ab,1)\nldab : input int, optional\n    Default: shape(ab,0)\nldb : input int, optional\n    Default: shape(b,0)\n\nReturns\n-------\nx : rank-2 array('d') with bounds (ldb,nrhs) and b storage\ninfo : int\n"
    pass

def dgebal():
    "ba,lo,hi,pivscale,info = dgebal(a,[scale,permute,overwrite_a])\n\nWrapper for ``dgebal``.\n\nParameters\n----------\na : input rank-2 array('d') with bounds (m,n)\n\nOther Parameters\n----------------\nscale : input int, optional\n    Default: 0\npermute : input int, optional\n    Default: 0\noverwrite_a : input int, optional\n    Default: 0\n\nReturns\n-------\nba : rank-2 array('d') with bounds (m,n) and a storage\nlo : int\nhi : int\npivscale : rank-1 array('d') with bounds (n)\ninfo : int\n"
    pass

def dgecon():
    "rcond,info = dgecon(a,anorm,[norm])\n\nWrapper for ``dgecon``.\n\nParameters\n----------\na : input rank-2 array('d') with bounds (n,n)\nanorm : input float\n\nOther Parameters\n----------------\nnorm : input string(len=1), optional\n    Default: '1'\n\nReturns\n-------\nrcond : float\ninfo : int\n"
    pass

def dgees():
    "t,sdim,wr,wi,vs,work,info = dgees(dselect,a,[compute_v,sort_t,lwork,dselect_extra_args,overwrite_a])\n\nWrapper for ``dgees``.\n\nParameters\n----------\ndselect : call-back function\na : input rank-2 array('d') with bounds (n,n)\n\nOther Parameters\n----------------\ncompute_v : input int, optional\n    Default: 1\nsort_t : input int, optional\n    Default: 0\ndselect_extra_args : input tuple, optional\n    Default: ()\noverwrite_a : input int, optional\n    Default: 0\nlwork : input int, optional\n    Default: 3*n\n\nReturns\n-------\nt : rank-2 array('d') with bounds (n,n) and a storage\nsdim : int\nwr : rank-1 array('d') with bounds (n)\nwi : rank-1 array('d') with bounds (n)\nvs : rank-2 array('d') with bounds (ldvs,n)\nwork : rank-1 array('d') with bounds (MAX(lwork,1))\ninfo : int\n\nNotes\n-----\nCall-back functions::\n\n  def dselect(arg1,arg2): return dselect\n  Required arguments:\n    arg1 : input float\n    arg2 : input float\n  Return objects:\n    dselect : int\n"
    pass

def dgeev():
    "wr,wi,vl,vr,info = dgeev(a,[compute_vl,compute_vr,lwork,overwrite_a])\n\nWrapper for ``dgeev``.\n\nParameters\n----------\na : input rank-2 array('d') with bounds (n,n)\n\nOther Parameters\n----------------\ncompute_vl : input int, optional\n    Default: 1\ncompute_vr : input int, optional\n    Default: 1\noverwrite_a : input int, optional\n    Default: 0\nlwork : input int, optional\n    Default: 4*n\n\nReturns\n-------\nwr : rank-1 array('d') with bounds (n)\nwi : rank-1 array('d') with bounds (n)\nvl : rank-2 array('d') with bounds (ldvl,n)\nvr : rank-2 array('d') with bounds (ldvr,n)\ninfo : int\n"
    pass

def dgeev_lwork():
    'work,info = dgeev_lwork(n,[compute_vl,compute_vr])\n\nWrapper for ``dgeev_lwork``.\n\nParameters\n----------\nn : input int\n\nOther Parameters\n----------------\ncompute_vl : input int, optional\n    Default: 1\ncompute_vr : input int, optional\n    Default: 1\n\nReturns\n-------\nwork : float\ninfo : int\n'
    pass

def dgegv(*args, **kwds):
    "`dgegv` is deprecated!\nThe `*gegv` family of routines has been deprecated in\nLAPACK 3.6.0 in favor of the `*ggev` family of routines.\nThe corresponding wrappers will be removed from SciPy in\na future release.\n\nalphar,alphai,beta,vl,vr,info = dgegv(a,b,[compute_vl,compute_vr,lwork,overwrite_a,overwrite_b])\n\nWrapper for ``dgegv``.\n\nParameters\n----------\na : input rank-2 array('d') with bounds (n,n)\nb : input rank-2 array('d') with bounds (n,n)\n\nOther Parameters\n----------------\ncompute_vl : input int, optional\n    Default: 1\ncompute_vr : input int, optional\n    Default: 1\noverwrite_a : input int, optional\n    Default: 0\noverwrite_b : input int, optional\n    Default: 0\nlwork : input int, optional\n    Default: 8*n\n\nReturns\n-------\nalphar : rank-1 array('d') with bounds (n)\nalphai : rank-1 array('d') with bounds (n)\nbeta : rank-1 array('d') with bounds (n)\nvl : rank-2 array('d') with bounds (ldvl,n)\nvr : rank-2 array('d') with bounds (ldvr,n)\ninfo : int\n"
    pass

def dgehrd():
    "ht,tau,info = dgehrd(a,[lo,hi,lwork,overwrite_a])\n\nWrapper for ``dgehrd``.\n\nParameters\n----------\na : input rank-2 array('d') with bounds (n,n)\n\nOther Parameters\n----------------\nlo : input int, optional\n    Default: 0\nhi : input int, optional\n    Default: n-1\noverwrite_a : input int, optional\n    Default: 0\nlwork : input int, optional\n    Default: MAX(n,1)\n\nReturns\n-------\nht : rank-2 array('d') with bounds (n,n) and a storage\ntau : rank-1 array('d') with bounds (n - 1)\ninfo : int\n"
    pass

def dgehrd_lwork():
    'work,info = dgehrd_lwork(n,[lo,hi])\n\nWrapper for ``dgehrd_lwork``.\n\nParameters\n----------\nn : input int\n\nOther Parameters\n----------------\nlo : input int, optional\n    Default: 0\nhi : input int, optional\n    Default: n-1\n\nReturns\n-------\nwork : float\ninfo : int\n'
    pass

def dgelsd():
    "x,s,rank,info = dgelsd(a,b,lwork,size_iwork,[cond,overwrite_a,overwrite_b])\n\nWrapper for ``dgelsd``.\n\nParameters\n----------\na : input rank-2 array('d') with bounds (m,n)\nb : input rank-2 array('d') with bounds (maxmn,nrhs)\nlwork : input int\nsize_iwork : input int\n\nOther Parameters\n----------------\noverwrite_a : input int, optional\n    Default: 0\noverwrite_b : input int, optional\n    Default: 0\ncond : input float, optional\n    Default: -1.0\n\nReturns\n-------\nx : rank-2 array('d') with bounds (maxmn,nrhs) and b storage\ns : rank-1 array('d') with bounds (minmn)\nrank : int\ninfo : int\n"
    pass

def dgelsd_lwork():
    'work,iwork,info = dgelsd_lwork(m,n,nrhs,[cond,lwork])\n\nWrapper for ``dgelsd_lwork``.\n\nParameters\n----------\nm : input int\nn : input int\nnrhs : input int\n\nOther Parameters\n----------------\ncond : input float, optional\n    Default: -1.0\nlwork : input int, optional\n    Default: -1\n\nReturns\n-------\nwork : float\niwork : int\ninfo : int\n'
    pass

def dgelss():
    "v,x,s,rank,work,info = dgelss(a,b,[cond,lwork,overwrite_a,overwrite_b])\n\nWrapper for ``dgelss``.\n\nParameters\n----------\na : input rank-2 array('d') with bounds (m,n)\nb : input rank-2 array('d') with bounds (maxmn,nrhs)\n\nOther Parameters\n----------------\noverwrite_a : input int, optional\n    Default: 0\noverwrite_b : input int, optional\n    Default: 0\ncond : input float, optional\n    Default: -1.0\nlwork : input int, optional\n    Default: 3*minmn+MAX(2*minmn,MAX(maxmn,nrhs))\n\nReturns\n-------\nv : rank-2 array('d') with bounds (m,n) and a storage\nx : rank-2 array('d') with bounds (maxmn,nrhs) and b storage\ns : rank-1 array('d') with bounds (minmn)\nrank : int\nwork : rank-1 array('d') with bounds (MAX(lwork,1))\ninfo : int\n"
    pass

def dgelss_lwork():
    'work,info = dgelss_lwork(m,n,nrhs,[cond,lwork])\n\nWrapper for ``dgelss_lwork``.\n\nParameters\n----------\nm : input int\nn : input int\nnrhs : input int\n\nOther Parameters\n----------------\ncond : input float, optional\n    Default: -1.0\nlwork : input int, optional\n    Default: -1\n\nReturns\n-------\nwork : float\ninfo : int\n'
    pass

def dgelsy():
    "v,x,j,rank,info = dgelsy(a,b,jptv,cond,lwork,[overwrite_a,overwrite_b])\n\nWrapper for ``dgelsy``.\n\nParameters\n----------\na : input rank-2 array('d') with bounds (m,n)\nb : input rank-2 array('d') with bounds (maxmn,nrhs)\njptv : input rank-1 array('i') with bounds (n)\ncond : input float\nlwork : input int\n\nOther Parameters\n----------------\noverwrite_a : input int, optional\n    Default: 0\noverwrite_b : input int, optional\n    Default: 0\n\nReturns\n-------\nv : rank-2 array('d') with bounds (m,n) and a storage\nx : rank-2 array('d') with bounds (maxmn,nrhs) and b storage\nj : rank-1 array('i') with bounds (n) and jptv storage\nrank : int\ninfo : int\n"
    pass

def dgelsy_lwork():
    'work,info = dgelsy_lwork(m,n,nrhs,cond,[lwork])\n\nWrapper for ``dgelsy_lwork``.\n\nParameters\n----------\nm : input int\nn : input int\nnrhs : input int\ncond : input float\n\nOther Parameters\n----------------\nlwork : input int, optional\n    Default: -1\n\nReturns\n-------\nwork : float\ninfo : int\n'
    pass

def dgeqp3():
    "qr,jpvt,tau,work,info = dgeqp3(a,[lwork,overwrite_a])\n\nWrapper for ``dgeqp3``.\n\nParameters\n----------\na : input rank-2 array('d') with bounds (m,n)\n\nOther Parameters\n----------------\noverwrite_a : input int, optional\n    Default: 0\nlwork : input int, optional\n    Default: 3*(n+1)\n\nReturns\n-------\nqr : rank-2 array('d') with bounds (m,n) and a storage\njpvt : rank-1 array('i') with bounds (n)\ntau : rank-1 array('d') with bounds (MIN(m,n))\nwork : rank-1 array('d') with bounds (MAX(lwork,1))\ninfo : int\n"
    pass

def dgeqrf():
    "qr,tau,work,info = dgeqrf(a,[lwork,overwrite_a])\n\nWrapper for ``dgeqrf``.\n\nParameters\n----------\na : input rank-2 array('d') with bounds (m,n)\n\nOther Parameters\n----------------\noverwrite_a : input int, optional\n    Default: 0\nlwork : input int, optional\n    Default: 3*n\n\nReturns\n-------\nqr : rank-2 array('d') with bounds (m,n) and a storage\ntau : rank-1 array('d') with bounds (MIN(m,n))\nwork : rank-1 array('d') with bounds (MAX(lwork,1))\ninfo : int\n"
    pass

def dgerqf():
    "qr,tau,work,info = dgerqf(a,[lwork,overwrite_a])\n\nWrapper for ``dgerqf``.\n\nParameters\n----------\na : input rank-2 array('d') with bounds (m,n)\n\nOther Parameters\n----------------\noverwrite_a : input int, optional\n    Default: 0\nlwork : input int, optional\n    Default: 3*m\n\nReturns\n-------\nqr : rank-2 array('d') with bounds (m,n) and a storage\ntau : rank-1 array('d') with bounds (MIN(m,n))\nwork : rank-1 array('d') with bounds (MAX(lwork,1))\ninfo : int\n"
    pass

def dgesdd():
    "u,s,vt,info = dgesdd(a,[compute_uv,full_matrices,lwork,overwrite_a])\n\nWrapper for ``dgesdd``.\n\nParameters\n----------\na : input rank-2 array('d') with bounds (m,n)\n\nOther Parameters\n----------------\noverwrite_a : input int, optional\n    Default: 0\ncompute_uv : input int, optional\n    Default: 1\nfull_matrices : input int, optional\n    Default: 1\nlwork : input int, optional\n    Default: (compute_uv?4*minmn*minmn+MAX(m,n)+9*minmn:MAX(14*minmn+4,10*minmn+2+25*(25+8))+MAX(m,n))\n\nReturns\n-------\nu : rank-2 array('d') with bounds (u0,u1)\ns : rank-1 array('d') with bounds (minmn)\nvt : rank-2 array('d') with bounds (vt0,vt1)\ninfo : int\n"
    pass

def dgesdd_lwork():
    'work,info = dgesdd_lwork(m,n,[compute_uv,full_matrices])\n\nWrapper for ``dgesdd_lwork``.\n\nParameters\n----------\nm : input int\nn : input int\n\nOther Parameters\n----------------\ncompute_uv : input int, optional\n    Default: 1\nfull_matrices : input int, optional\n    Default: 1\n\nReturns\n-------\nwork : float\ninfo : int\n'
    pass

def dgesv():
    "lu,piv,x,info = dgesv(a,b,[overwrite_a,overwrite_b])\n\nWrapper for ``dgesv``.\n\nParameters\n----------\na : input rank-2 array('d') with bounds (n,n)\nb : input rank-2 array('d') with bounds (n,nrhs)\n\nOther Parameters\n----------------\noverwrite_a : input int, optional\n    Default: 0\noverwrite_b : input int, optional\n    Default: 0\n\nReturns\n-------\nlu : rank-2 array('d') with bounds (n,n) and a storage\npiv : rank-1 array('i') with bounds (n)\nx : rank-2 array('d') with bounds (n,nrhs) and b storage\ninfo : int\n"
    pass

def dgesvd():
    "u,s,vt,info = dgesvd(a,[compute_uv,full_matrices,lwork,overwrite_a])\n\nWrapper for ``dgesvd``.\n\nParameters\n----------\na : input rank-2 array('d') with bounds (m,n)\n\nOther Parameters\n----------------\noverwrite_a : input int, optional\n    Default: 0\ncompute_uv : input int, optional\n    Default: 1\nfull_matrices : input int, optional\n    Default: 1\nlwork : input int, optional\n    Default: MAX(1,MAX(3*minmn+MAX(m,n),5*minmn))\n\nReturns\n-------\nu : rank-2 array('d') with bounds (u0,u1)\ns : rank-1 array('d') with bounds (minmn)\nvt : rank-2 array('d') with bounds (vt0,vt1)\ninfo : int\n"
    pass

def dgesvd_lwork():
    'work,info = dgesvd_lwork(m,n,[compute_uv,full_matrices])\n\nWrapper for ``dgesvd_lwork``.\n\nParameters\n----------\nm : input int\nn : input int\n\nOther Parameters\n----------------\ncompute_uv : input int, optional\n    Default: 1\nfull_matrices : input int, optional\n    Default: 1\n\nReturns\n-------\nwork : float\ninfo : int\n'
    pass

def dgesvx():
    "as,lu,ipiv,equed,rs,cs,bs,x,rcond,ferr,berr,info = dgesvx(a,b,[fact,trans,af,ipiv,equed,r,c,overwrite_a,overwrite_b])\n\nWrapper for ``dgesvx``.\n\nParameters\n----------\na : input rank-2 array('d') with bounds (n,n)\nb : input rank-2 array('d') with bounds (n,nrhs)\n\nOther Parameters\n----------------\nfact : input string(len=1), optional\n    Default: 'E'\ntrans : input string(len=1), optional\n    Default: 'N'\noverwrite_a : input int, optional\n    Default: 0\naf : input rank-2 array('d') with bounds (n,n)\nipiv : input rank-1 array('i') with bounds (n)\nequed : input string(len=1), optional\n    Default: 'B'\nr : input rank-1 array('d') with bounds (n)\nc : input rank-1 array('d') with bounds (n)\noverwrite_b : input int, optional\n    Default: 0\n\nReturns\n-------\nas : rank-2 array('d') with bounds (n,n) and a storage\nlu : rank-2 array('d') with bounds (n,n) and af storage\nipiv : rank-1 array('i') with bounds (n)\nequed : string(len=1)\nrs : rank-1 array('d') with bounds (n) and r storage\ncs : rank-1 array('d') with bounds (n) and c storage\nbs : rank-2 array('d') with bounds (n,nrhs) and b storage\nx : rank-2 array('d') with bounds (n,nrhs)\nrcond : float\nferr : rank-1 array('d') with bounds (nrhs)\nberr : rank-1 array('d') with bounds (nrhs)\ninfo : int\n"
    pass

def dgetrf():
    "lu,piv,info = dgetrf(a,[overwrite_a])\n\nWrapper for ``dgetrf``.\n\nParameters\n----------\na : input rank-2 array('d') with bounds (m,n)\n\nOther Parameters\n----------------\noverwrite_a : input int, optional\n    Default: 0\n\nReturns\n-------\nlu : rank-2 array('d') with bounds (m,n) and a storage\npiv : rank-1 array('i') with bounds (MIN(m,n))\ninfo : int\n"
    pass

def dgetri():
    "inv_a,info = dgetri(lu,piv,[lwork,overwrite_lu])\n\nWrapper for ``dgetri``.\n\nParameters\n----------\nlu : input rank-2 array('d') with bounds (n,n)\npiv : input rank-1 array('i') with bounds (n)\n\nOther Parameters\n----------------\noverwrite_lu : input int, optional\n    Default: 0\nlwork : input int, optional\n    Default: 3*n\n\nReturns\n-------\ninv_a : rank-2 array('d') with bounds (n,n) and lu storage\ninfo : int\n"
    pass

def dgetri_lwork():
    'work,info = dgetri_lwork(n)\n\nWrapper for ``dgetri_lwork``.\n\nParameters\n----------\nn : input int\n\nReturns\n-------\nwork : float\ninfo : int\n'
    pass

def dgetrs():
    "x,info = dgetrs(lu,piv,b,[trans,overwrite_b])\n\nWrapper for ``dgetrs``.\n\nParameters\n----------\nlu : input rank-2 array('d') with bounds (n,n)\npiv : input rank-1 array('i') with bounds (n)\nb : input rank-2 array('d') with bounds (n,nrhs)\n\nOther Parameters\n----------------\noverwrite_b : input int, optional\n    Default: 0\ntrans : input int, optional\n    Default: 0\n\nReturns\n-------\nx : rank-2 array('d') with bounds (n,nrhs) and b storage\ninfo : int\n"
    pass

def dgges():
    "a,b,sdim,alphar,alphai,beta,vsl,vsr,work,info = dgges(dselect,a,b,[jobvsl,jobvsr,sort_t,ldvsl,ldvsr,lwork,dselect_extra_args,overwrite_a,overwrite_b])\n\nWrapper for ``dgges``.\n\nParameters\n----------\ndselect : call-back function\na : input rank-2 array('d') with bounds (lda,n)\nb : input rank-2 array('d') with bounds (ldb,n)\n\nOther Parameters\n----------------\njobvsl : input int, optional\n    Default: 1\njobvsr : input int, optional\n    Default: 1\nsort_t : input int, optional\n    Default: 0\ndselect_extra_args : input tuple, optional\n    Default: ()\noverwrite_a : input int, optional\n    Default: 0\noverwrite_b : input int, optional\n    Default: 0\nldvsl : input int, optional\n    Default: ((jobvsl==1)?n:1)\nldvsr : input int, optional\n    Default: ((jobvsr==1)?n:1)\nlwork : input int, optional\n    Default: 8*n+16\n\nReturns\n-------\na : rank-2 array('d') with bounds (lda,n)\nb : rank-2 array('d') with bounds (ldb,n)\nsdim : int\nalphar : rank-1 array('d') with bounds (n)\nalphai : rank-1 array('d') with bounds (n)\nbeta : rank-1 array('d') with bounds (n)\nvsl : rank-2 array('d') with bounds (ldvsl,n)\nvsr : rank-2 array('d') with bounds (ldvsr,n)\nwork : rank-1 array('d') with bounds (MAX(lwork,1))\ninfo : int\n\nNotes\n-----\nCall-back functions::\n\n  def dselect(alphar,alphai,beta): return dselect\n  Required arguments:\n    alphar : input float\n    alphai : input float\n    beta : input float\n  Return objects:\n    dselect : int\n"
    pass

def dggev():
    "alphar,alphai,beta,vl,vr,work,info = dggev(a,b,[compute_vl,compute_vr,lwork,overwrite_a,overwrite_b])\n\nWrapper for ``dggev``.\n\nParameters\n----------\na : input rank-2 array('d') with bounds (n,n)\nb : input rank-2 array('d') with bounds (n,n)\n\nOther Parameters\n----------------\ncompute_vl : input int, optional\n    Default: 1\ncompute_vr : input int, optional\n    Default: 1\noverwrite_a : input int, optional\n    Default: 0\noverwrite_b : input int, optional\n    Default: 0\nlwork : input int, optional\n    Default: 8*n\n\nReturns\n-------\nalphar : rank-1 array('d') with bounds (n)\nalphai : rank-1 array('d') with bounds (n)\nbeta : rank-1 array('d') with bounds (n)\nvl : rank-2 array('d') with bounds (ldvl,n)\nvr : rank-2 array('d') with bounds (ldvr,n)\nwork : rank-1 array('d') with bounds (MAX(lwork,1))\ninfo : int\n"
    pass

def dgtsv():
    "du2,d,du,x,info = dgtsv(dl,d,du,b,[overwrite_dl,overwrite_d,overwrite_du,overwrite_b])\n\nWrapper for ``dgtsv``.\n\nParameters\n----------\ndl : input rank-1 array('d') with bounds (n - 1)\nd : input rank-1 array('d') with bounds (n)\ndu : input rank-1 array('d') with bounds (n - 1)\nb : input rank-2 array('d') with bounds (n,nrhs)\n\nOther Parameters\n----------------\noverwrite_dl : input int, optional\n    Default: 0\noverwrite_d : input int, optional\n    Default: 0\noverwrite_du : input int, optional\n    Default: 0\noverwrite_b : input int, optional\n    Default: 0\n\nReturns\n-------\ndu2 : rank-1 array('d') with bounds (n - 1) and dl storage\nd : rank-1 array('d') with bounds (n)\ndu : rank-1 array('d') with bounds (n - 1)\nx : rank-2 array('d') with bounds (n,nrhs) and b storage\ninfo : int\n"
    pass

def dlamch():
    'dlamch = dlamch(cmach)\n\nWrapper for ``dlamch``.\n\nParameters\n----------\ncmach : input string(len=1)\n\nReturns\n-------\ndlamch : float\n'
    pass

def dlange():
    "n2 = dlange(norm,a)\n\nWrapper for ``dlange``.\n\nParameters\n----------\nnorm : input string(len=1)\na : input rank-2 array('d') with bounds (m,n)\n\nReturns\n-------\nn2 : float\n"
    pass

def dlarf():
    "c = dlarf(v,tau,c,work,[side,incv,overwrite_c])\n\nWrapper for ``dlarf``.\n\nParameters\n----------\nv : input rank-1 array('d') with bounds (*)\ntau : input float\nc : input rank-2 array('d') with bounds (m,n)\nwork : input rank-1 array('d') with bounds (*)\n\nOther Parameters\n----------------\nside : input string(len=1), optional\n    Default: 'L'\nincv : input int, optional\n    Default: 1\noverwrite_c : input int, optional\n    Default: 0\n\nReturns\n-------\nc : rank-2 array('d') with bounds (m,n)\n"
    pass

def dlarfg():
    "alpha,x,tau = dlarfg(n,alpha,x,[incx,overwrite_x])\n\nWrapper for ``dlarfg``.\n\nParameters\n----------\nn : input int\nalpha : input float\nx : input rank-1 array('d') with bounds (*)\n\nOther Parameters\n----------------\noverwrite_x : input int, optional\n    Default: 0\nincx : input int, optional\n    Default: 1\n\nReturns\n-------\nalpha : float\nx : rank-1 array('d') with bounds (*)\ntau : float\n"
    pass

def dlartg():
    'cs,sn,r = dlartg(f,g)\n\nWrapper for ``dlartg``.\n\nParameters\n----------\nf : input float\ng : input float\n\nReturns\n-------\ncs : float\nsn : float\nr : float\n'
    pass

def dlasd4():
    "delta,sigma,work,info = dlasd4(i,d,z,[rho])\n\nWrapper for ``dlasd4``.\n\nParameters\n----------\ni : input int\nd : input rank-1 array('d') with bounds (n)\nz : input rank-1 array('d') with bounds (n)\n\nOther Parameters\n----------------\nrho : input float, optional\n    Default: 1.0\n\nReturns\n-------\ndelta : rank-1 array('d') with bounds (n)\nsigma : float\nwork : rank-1 array('d') with bounds (n)\ninfo : int\n"
    pass

def dlaswp():
    "a = dlaswp(a,piv,[k1,k2,off,inc,overwrite_a])\n\nWrapper for ``dlaswp``.\n\nParameters\n----------\na : input rank-2 array('d') with bounds (nrows,n)\npiv : input rank-1 array('i') with bounds (*)\n\nOther Parameters\n----------------\noverwrite_a : input int, optional\n    Default: 0\nk1 : input int, optional\n    Default: 0\nk2 : input int, optional\n    Default: len(piv)-1\noff : input int, optional\n    Default: 0\ninc : input int, optional\n    Default: 1\n\nReturns\n-------\na : rank-2 array('d') with bounds (nrows,n)\n"
    pass

def dlauum():
    "a,info = dlauum(c,[lower,overwrite_c])\n\nWrapper for ``dlauum``.\n\nParameters\n----------\nc : input rank-2 array('d') with bounds (n,n)\n\nOther Parameters\n----------------\noverwrite_c : input int, optional\n    Default: 0\nlower : input int, optional\n    Default: 0\n\nReturns\n-------\na : rank-2 array('d') with bounds (n,n) and c storage\ninfo : int\n"
    pass

def dorghr():
    "ht,info = dorghr(a,tau,[lo,hi,lwork,overwrite_a])\n\nWrapper for ``dorghr``.\n\nParameters\n----------\na : input rank-2 array('d') with bounds (n,n)\ntau : input rank-1 array('d') with bounds (n - 1)\n\nOther Parameters\n----------------\nlo : input int, optional\n    Default: 0\nhi : input int, optional\n    Default: n-1\noverwrite_a : input int, optional\n    Default: 0\nlwork : input int, optional\n    Default: hi-lo\n\nReturns\n-------\nht : rank-2 array('d') with bounds (n,n) and a storage\ninfo : int\n"
    pass

def dorghr_lwork():
    'work,info = dorghr_lwork(n,[lo,hi])\n\nWrapper for ``dorghr_lwork``.\n\nParameters\n----------\nn : input int\n\nOther Parameters\n----------------\nlo : input int, optional\n    Default: 0\nhi : input int, optional\n    Default: n-1\n\nReturns\n-------\nwork : float\ninfo : int\n'
    pass

def dorgqr():
    "q,work,info = dorgqr(a,tau,[lwork,overwrite_a])\n\nWrapper for ``dorgqr``.\n\nParameters\n----------\na : input rank-2 array('d') with bounds (m,n)\ntau : input rank-1 array('d') with bounds (k)\n\nOther Parameters\n----------------\noverwrite_a : input int, optional\n    Default: 0\nlwork : input int, optional\n    Default: 3*n\n\nReturns\n-------\nq : rank-2 array('d') with bounds (m,n) and a storage\nwork : rank-1 array('d') with bounds (MAX(lwork,1))\ninfo : int\n"
    pass

def dorgrq():
    "q,work,info = dorgrq(a,tau,[lwork,overwrite_a])\n\nWrapper for ``dorgrq``.\n\nParameters\n----------\na : input rank-2 array('d') with bounds (m,n)\ntau : input rank-1 array('d') with bounds (k)\n\nOther Parameters\n----------------\noverwrite_a : input int, optional\n    Default: 0\nlwork : input int, optional\n    Default: 3*m\n\nReturns\n-------\nq : rank-2 array('d') with bounds (m,n) and a storage\nwork : rank-1 array('d') with bounds (MAX(lwork,1))\ninfo : int\n"
    pass

def dormqr():
    "cq,work,info = dormqr(side,trans,a,tau,c,lwork,[overwrite_c])\n\nWrapper for ``dormqr``.\n\nParameters\n----------\nside : input string(len=1)\ntrans : input string(len=1)\na : input rank-2 array('d') with bounds (lda,k)\ntau : input rank-1 array('d') with bounds (k)\nc : input rank-2 array('d') with bounds (ldc,n)\nlwork : input int\n\nOther Parameters\n----------------\noverwrite_c : input int, optional\n    Default: 0\n\nReturns\n-------\ncq : rank-2 array('d') with bounds (ldc,n) and c storage\nwork : rank-1 array('d') with bounds (MAX(lwork,1))\ninfo : int\n"
    pass

def dpbsv():
    "c,x,info = dpbsv(ab,b,[lower,ldab,overwrite_ab,overwrite_b])\n\nWrapper for ``dpbsv``.\n\nParameters\n----------\nab : input rank-2 array('d') with bounds (ldab,n)\nb : input rank-2 array('d') with bounds (ldb,nrhs)\n\nOther Parameters\n----------------\nlower : input int, optional\n    Default: 0\noverwrite_ab : input int, optional\n    Default: 0\nldab : input int, optional\n    Default: shape(ab,0)\noverwrite_b : input int, optional\n    Default: 0\n\nReturns\n-------\nc : rank-2 array('d') with bounds (ldab,n) and ab storage\nx : rank-2 array('d') with bounds (ldb,nrhs) and b storage\ninfo : int\n"
    pass

def dpbtrf():
    "c,info = dpbtrf(ab,[lower,ldab,overwrite_ab])\n\nWrapper for ``dpbtrf``.\n\nParameters\n----------\nab : input rank-2 array('d') with bounds (ldab,n)\n\nOther Parameters\n----------------\nlower : input int, optional\n    Default: 0\noverwrite_ab : input int, optional\n    Default: 0\nldab : input int, optional\n    Default: shape(ab,0)\n\nReturns\n-------\nc : rank-2 array('d') with bounds (ldab,n) and ab storage\ninfo : int\n"
    pass

def dpbtrs():
    "x,info = dpbtrs(ab,b,[lower,ldab,overwrite_b])\n\nWrapper for ``dpbtrs``.\n\nParameters\n----------\nab : input rank-2 array('d') with bounds (ldab,n)\nb : input rank-2 array('d') with bounds (ldb,nrhs)\n\nOther Parameters\n----------------\nlower : input int, optional\n    Default: 0\nldab : input int, optional\n    Default: shape(ab,0)\noverwrite_b : input int, optional\n    Default: 0\n\nReturns\n-------\nx : rank-2 array('d') with bounds (ldb,nrhs) and b storage\ninfo : int\n"
    pass

def dpocon():
    "rcond,info = dpocon(a,anorm,[uplo])\n\nWrapper for ``dpocon``.\n\nParameters\n----------\na : input rank-2 array('d') with bounds (n,n)\nanorm : input float\n\nOther Parameters\n----------------\nuplo : input string(len=1), optional\n    Default: 'U'\n\nReturns\n-------\nrcond : float\ninfo : int\n"
    pass

def dposv():
    "c,x,info = dposv(a,b,[lower,overwrite_a,overwrite_b])\n\nWrapper for ``dposv``.\n\nParameters\n----------\na : input rank-2 array('d') with bounds (n,n)\nb : input rank-2 array('d') with bounds (n,nrhs)\n\nOther Parameters\n----------------\noverwrite_a : input int, optional\n    Default: 0\noverwrite_b : input int, optional\n    Default: 0\nlower : input int, optional\n    Default: 0\n\nReturns\n-------\nc : rank-2 array('d') with bounds (n,n) and a storage\nx : rank-2 array('d') with bounds (n,nrhs) and b storage\ninfo : int\n"
    pass

def dposvx():
    "a_s,lu,equed,s,b_s,x,rcond,ferr,berr,info = dposvx(a,b,[fact,af,equed,s,lower,overwrite_a,overwrite_b])\n\nWrapper for ``dposvx``.\n\nParameters\n----------\na : input rank-2 array('d') with bounds (n,n)\nb : input rank-2 array('d') with bounds (n,nrhs)\n\nOther Parameters\n----------------\nfact : input string(len=1), optional\n    Default: 'E'\noverwrite_a : input int, optional\n    Default: 0\naf : input rank-2 array('d') with bounds (n,n)\nequed : input string(len=1), optional\n    Default: 'Y'\ns : input rank-1 array('d') with bounds (n)\noverwrite_b : input int, optional\n    Default: 0\nlower : input int, optional\n    Default: 0\n\nReturns\n-------\na_s : rank-2 array('d') with bounds (n,n) and a storage\nlu : rank-2 array('d') with bounds (n,n) and af storage\nequed : string(len=1)\ns : rank-1 array('d') with bounds (n)\nb_s : rank-2 array('d') with bounds (n,nrhs) and b storage\nx : rank-2 array('d') with bounds (n,nrhs)\nrcond : float\nferr : rank-1 array('d') with bounds (nrhs)\nberr : rank-1 array('d') with bounds (nrhs)\ninfo : int\n"
    pass

def dpotrf():
    "c,info = dpotrf(a,[lower,clean,overwrite_a])\n\nWrapper for ``dpotrf``.\n\nParameters\n----------\na : input rank-2 array('d') with bounds (n,n)\n\nOther Parameters\n----------------\noverwrite_a : input int, optional\n    Default: 0\nlower : input int, optional\n    Default: 0\nclean : input int, optional\n    Default: 1\n\nReturns\n-------\nc : rank-2 array('d') with bounds (n,n) and a storage\ninfo : int\n"
    pass

def dpotri():
    "inv_a,info = dpotri(c,[lower,overwrite_c])\n\nWrapper for ``dpotri``.\n\nParameters\n----------\nc : input rank-2 array('d') with bounds (n,n)\n\nOther Parameters\n----------------\noverwrite_c : input int, optional\n    Default: 0\nlower : input int, optional\n    Default: 0\n\nReturns\n-------\ninv_a : rank-2 array('d') with bounds (n,n) and c storage\ninfo : int\n"
    pass

def dpotrs():
    "x,info = dpotrs(c,b,[lower,overwrite_b])\n\nWrapper for ``dpotrs``.\n\nParameters\n----------\nc : input rank-2 array('d') with bounds (n,n)\nb : input rank-2 array('d') with bounds (n,nrhs)\n\nOther Parameters\n----------------\noverwrite_b : input int, optional\n    Default: 0\nlower : input int, optional\n    Default: 0\n\nReturns\n-------\nx : rank-2 array('d') with bounds (n,nrhs) and b storage\ninfo : int\n"
    pass

def dptsv():
    "d,du,x,info = dptsv(d,e,b,[overwrite_d,overwrite_e,overwrite_b])\n\nWrapper for ``dptsv``.\n\nParameters\n----------\nd : input rank-1 array('d') with bounds (n)\ne : input rank-1 array('d') with bounds (n - 1)\nb : input rank-2 array('d') with bounds (n,nrhs)\n\nOther Parameters\n----------------\noverwrite_d : input int, optional\n    Default: 0\noverwrite_e : input int, optional\n    Default: 0\noverwrite_b : input int, optional\n    Default: 0\n\nReturns\n-------\nd : rank-1 array('d') with bounds (n)\ndu : rank-1 array('d') with bounds (n - 1) and e storage\nx : rank-2 array('d') with bounds (n,nrhs) and b storage\ninfo : int\n"
    pass

def dsbev():
    "w,z,info = dsbev(ab,[compute_v,lower,ldab,overwrite_ab])\n\nWrapper for ``dsbev``.\n\nParameters\n----------\nab : input rank-2 array('d') with bounds (ldab,n)\n\nOther Parameters\n----------------\noverwrite_ab : input int, optional\n    Default: 1\ncompute_v : input int, optional\n    Default: 1\nlower : input int, optional\n    Default: 0\nldab : input int, optional\n    Default: shape(ab,0)\n\nReturns\n-------\nw : rank-1 array('d') with bounds (n)\nz : rank-2 array('d') with bounds (ldz,ldz)\ninfo : int\n"
    pass

def dsbevd():
    "w,z,info = dsbevd(ab,[compute_v,lower,ldab,liwork,overwrite_ab])\n\nWrapper for ``dsbevd``.\n\nParameters\n----------\nab : input rank-2 array('d') with bounds (ldab,n)\n\nOther Parameters\n----------------\noverwrite_ab : input int, optional\n    Default: 1\ncompute_v : input int, optional\n    Default: 1\nlower : input int, optional\n    Default: 0\nldab : input int, optional\n    Default: shape(ab,0)\nliwork : input int, optional\n    Default: (compute_v?3+5*n:1)\n\nReturns\n-------\nw : rank-1 array('d') with bounds (n)\nz : rank-2 array('d') with bounds (ldz,ldz)\ninfo : int\n"
    pass

def dsbevx():
    "w,z,m,ifail,info = dsbevx(ab,vl,vu,il,iu,[ldab,compute_v,range,lower,abstol,mmax,overwrite_ab])\n\nWrapper for ``dsbevx``.\n\nParameters\n----------\nab : input rank-2 array('d') with bounds (ldab,n)\nvl : input float\nvu : input float\nil : input int\niu : input int\n\nOther Parameters\n----------------\noverwrite_ab : input int, optional\n    Default: 1\nldab : input int, optional\n    Default: shape(ab,0)\ncompute_v : input int, optional\n    Default: 1\nrange : input int, optional\n    Default: 0\nlower : input int, optional\n    Default: 0\nabstol : input float, optional\n    Default: 0.0\nmmax : input int, optional\n    Default: (compute_v?(range==2?(iu-il+1):n):1)\n\nReturns\n-------\nw : rank-1 array('d') with bounds (n)\nz : rank-2 array('d') with bounds (ldz,mmax)\nm : int\nifail : rank-1 array('i') with bounds ((compute_v?n:1))\ninfo : int\n"
    pass

def dsyev():
    "w,v,info = dsyev(a,[compute_v,lower,lwork,overwrite_a])\n\nWrapper for ``dsyev``.\n\nParameters\n----------\na : input rank-2 array('d') with bounds (n,n)\n\nOther Parameters\n----------------\ncompute_v : input int, optional\n    Default: 1\nlower : input int, optional\n    Default: 0\noverwrite_a : input int, optional\n    Default: 0\nlwork : input int, optional\n    Default: 3*n-1\n\nReturns\n-------\nw : rank-1 array('d') with bounds (n)\nv : rank-2 array('d') with bounds (n,n) and a storage\ninfo : int\n"
    pass

def dsyevd():
    "w,v,info = dsyevd(a,[compute_v,lower,lwork,overwrite_a])\n\nWrapper for ``dsyevd``.\n\nParameters\n----------\na : input rank-2 array('d') with bounds (n,n)\n\nOther Parameters\n----------------\ncompute_v : input int, optional\n    Default: 1\nlower : input int, optional\n    Default: 0\noverwrite_a : input int, optional\n    Default: 0\nlwork : input int, optional\n    Default: (compute_v?1+6*n+2*n*n:2*n+1)\n\nReturns\n-------\nw : rank-1 array('d') with bounds (n)\nv : rank-2 array('d') with bounds (n,n) and a storage\ninfo : int\n"
    pass

def dsyevr():
    "w,z,info = dsyevr(a,[jobz,range,uplo,il,iu,lwork,overwrite_a])\n\nWrapper for ``dsyevr``.\n\nParameters\n----------\na : input rank-2 array('d') with bounds (n,n)\n\nOther Parameters\n----------------\njobz : input string(len=1), optional\n    Default: 'V'\nrange : input string(len=1), optional\n    Default: 'A'\nuplo : input string(len=1), optional\n    Default: 'L'\noverwrite_a : input int, optional\n    Default: 0\nil : input int, optional\n    Default: 1\niu : input int, optional\n    Default: n\nlwork : input int, optional\n    Default: 26*n\n\nReturns\n-------\nw : rank-1 array('d') with bounds (n)\nz : rank-2 array('d') with bounds (n,m)\ninfo : int\n"
    pass

def dsygv():
    "a,w,info = dsygv(a,b,[itype,jobz,uplo,overwrite_a,overwrite_b])\n\nWrapper for ``dsygv``.\n\nParameters\n----------\na : input rank-2 array('d') with bounds (n,n)\nb : input rank-2 array('d') with bounds (n,n)\n\nOther Parameters\n----------------\nitype : input int, optional\n    Default: 1\njobz : input string(len=1), optional\n    Default: 'V'\nuplo : input string(len=1), optional\n    Default: 'L'\noverwrite_a : input int, optional\n    Default: 0\noverwrite_b : input int, optional\n    Default: 0\n\nReturns\n-------\na : rank-2 array('d') with bounds (n,n)\nw : rank-1 array('d') with bounds (n)\ninfo : int\n"
    pass

def dsygvd():
    "a,w,info = dsygvd(a,b,[itype,jobz,uplo,lwork,overwrite_a,overwrite_b])\n\nWrapper for ``dsygvd``.\n\nParameters\n----------\na : input rank-2 array('d') with bounds (n,n)\nb : input rank-2 array('d') with bounds (n,n)\n\nOther Parameters\n----------------\nitype : input int, optional\n    Default: 1\njobz : input string(len=1), optional\n    Default: 'V'\nuplo : input string(len=1), optional\n    Default: 'L'\noverwrite_a : input int, optional\n    Default: 0\noverwrite_b : input int, optional\n    Default: 0\nlwork : input int, optional\n    Default: 1+6*n+2*n*n\n\nReturns\n-------\na : rank-2 array('d') with bounds (n,n)\nw : rank-1 array('d') with bounds (n)\ninfo : int\n"
    pass

def dsygvx():
    "w,z,ifail,info = dsygvx(a,b,iu,[itype,jobz,uplo,il,lwork,overwrite_a,overwrite_b])\n\nWrapper for ``dsygvx``.\n\nParameters\n----------\na : input rank-2 array('d') with bounds (n,n)\nb : input rank-2 array('d') with bounds (n,n)\niu : input int\n\nOther Parameters\n----------------\nitype : input int, optional\n    Default: 1\njobz : input string(len=1), optional\n    Default: 'V'\nuplo : input string(len=1), optional\n    Default: 'L'\noverwrite_a : input int, optional\n    Default: 0\noverwrite_b : input int, optional\n    Default: 0\nil : input int, optional\n    Default: 1\nlwork : input int, optional\n    Default: 8*n\n\nReturns\n-------\nw : rank-1 array('d') with bounds (n)\nz : rank-2 array('d') with bounds (n,m)\nifail : rank-1 array('i') with bounds (n)\ninfo : int\n"
    pass

def dsysv():
    "udut,ipiv,x,info = dsysv(a,b,[lwork,lower,overwrite_a,overwrite_b])\n\nWrapper for ``dsysv``.\n\nParameters\n----------\na : input rank-2 array('d') with bounds (n,n)\nb : input rank-2 array('d') with bounds (n,nrhs)\n\nOther Parameters\n----------------\noverwrite_a : input int, optional\n    Default: 0\noverwrite_b : input int, optional\n    Default: 0\nlwork : input int, optional\n    Default: n\nlower : input int, optional\n    Default: 0\n\nReturns\n-------\nudut : rank-2 array('d') with bounds (n,n) and a storage\nipiv : rank-1 array('i') with bounds (n)\nx : rank-2 array('d') with bounds (n,nrhs) and b storage\ninfo : int\n"
    pass

def dsysv_lwork():
    'work,info = dsysv_lwork(n,[lower])\n\nWrapper for ``dsysv_lwork``.\n\nParameters\n----------\nn : input int\n\nOther Parameters\n----------------\nlower : input int, optional\n    Default: 0\n\nReturns\n-------\nwork : float\ninfo : int\n'
    pass

def dsysvx():
    "a_s,udut,ipiv,b_s,x,rcond,ferr,berr,info = dsysvx(a,b,[af,ipiv,lwork,factored,lower,overwrite_a,overwrite_b])\n\nWrapper for ``dsysvx``.\n\nParameters\n----------\na : input rank-2 array('d') with bounds (n,n)\nb : input rank-2 array('d') with bounds (n,nrhs)\n\nOther Parameters\n----------------\noverwrite_a : input int, optional\n    Default: 0\naf : input rank-2 array('d') with bounds (n,n)\nipiv : input rank-1 array('i') with bounds (n)\noverwrite_b : input int, optional\n    Default: 0\nlwork : input int, optional\n    Default: 3*n\nfactored : input int, optional\n    Default: 0\nlower : input int, optional\n    Default: 0\n\nReturns\n-------\na_s : rank-2 array('d') with bounds (n,n) and a storage\nudut : rank-2 array('d') with bounds (n,n) and af storage\nipiv : rank-1 array('i') with bounds (n)\nb_s : rank-2 array('d') with bounds (n,nrhs) and b storage\nx : rank-2 array('d') with bounds (n,nrhs)\nrcond : float\nferr : rank-1 array('d') with bounds (nrhs)\nberr : rank-1 array('d') with bounds (nrhs)\ninfo : int\n"
    pass

def dsysvx_lwork():
    'work,info = dsysvx_lwork(n,[lower])\n\nWrapper for ``dsysvx_lwork``.\n\nParameters\n----------\nn : input int\n\nOther Parameters\n----------------\nlower : input int, optional\n    Default: 0\n\nReturns\n-------\nwork : float\ninfo : int\n'
    pass

def dtgsen():
    "a,b,alphar,alphai,beta,q,z,m,pl,pr,dif,work,iwork,info = dtgsen(select,a,b,q,z,[lwork,liwork,overwrite_a,overwrite_b,overwrite_q,overwrite_z])\n\nWrapper for ``dtgsen``.\n\nParameters\n----------\nselect : input rank-1 array('i') with bounds (n)\na : input rank-2 array('d') with bounds (lda,n)\nb : input rank-2 array('d') with bounds (ldb,n)\nq : input rank-2 array('d') with bounds (ldq,n)\nz : input rank-2 array('d') with bounds (ldz,n)\n\nOther Parameters\n----------------\noverwrite_a : input int, optional\n    Default: 0\noverwrite_b : input int, optional\n    Default: 0\noverwrite_q : input int, optional\n    Default: 0\noverwrite_z : input int, optional\n    Default: 0\nlwork : input int, optional\n    Default: MAX(4*n+16,2*m*(n-m))\nliwork : input int, optional\n    Default: n+6\n\nReturns\n-------\na : rank-2 array('d') with bounds (lda,n)\nb : rank-2 array('d') with bounds (ldb,n)\nalphar : rank-1 array('d') with bounds (n)\nalphai : rank-1 array('d') with bounds (n)\nbeta : rank-1 array('d') with bounds (n)\nq : rank-2 array('d') with bounds (ldq,n)\nz : rank-2 array('d') with bounds (ldz,n)\nm : int\npl : float\npr : float\ndif : rank-1 array('d') with bounds (2)\nwork : rank-1 array('d') with bounds (MAX(lwork,1))\niwork : rank-1 array('i') with bounds (MAX(1,liwork))\ninfo : int\n"
    pass

def dtrsyl():
    "x,scale,info = dtrsyl(a,b,c,[trana,tranb,isgn,overwrite_c])\n\nWrapper for ``dtrsyl``.\n\nParameters\n----------\na : input rank-2 array('d') with bounds (m,m)\nb : input rank-2 array('d') with bounds (n,n)\nc : input rank-2 array('d') with bounds (m,n)\n\nOther Parameters\n----------------\ntrana : input string(len=1), optional\n    Default: 'N'\ntranb : input string(len=1), optional\n    Default: 'N'\nisgn : input int, optional\n    Default: 1\noverwrite_c : input int, optional\n    Default: 0\n\nReturns\n-------\nx : rank-2 array('d') with bounds (m,n) and c storage\nscale : float\ninfo : int\n"
    pass

def dtrtri():
    "inv_c,info = dtrtri(c,[lower,unitdiag,overwrite_c])\n\nWrapper for ``dtrtri``.\n\nParameters\n----------\nc : input rank-2 array('d') with bounds (n,n)\n\nOther Parameters\n----------------\noverwrite_c : input int, optional\n    Default: 0\nlower : input int, optional\n    Default: 0\nunitdiag : input int, optional\n    Default: 0\n\nReturns\n-------\ninv_c : rank-2 array('d') with bounds (n,n) and c storage\ninfo : int\n"
    pass

def dtrtrs():
    "x,info = dtrtrs(a,b,[lower,trans,unitdiag,lda,overwrite_b])\n\nWrapper for ``dtrtrs``.\n\nParameters\n----------\na : input rank-2 array('d') with bounds (lda,n)\nb : input rank-2 array('d') with bounds (ldb,nrhs)\n\nOther Parameters\n----------------\nlower : input int, optional\n    Default: 0\ntrans : input int, optional\n    Default: 0\nunitdiag : input int, optional\n    Default: 0\nlda : input int, optional\n    Default: shape(a,0)\noverwrite_b : input int, optional\n    Default: 0\n\nReturns\n-------\nx : rank-2 array('d') with bounds (ldb,nrhs) and b storage\ninfo : int\n"
    pass

def ilaver():
    'major,minor,patch = ilaver()\n\nWrapper for ``ilaver``.\n\nReturns\n-------\nmajor : int\nminor : int\npatch : int\n'
    pass

def sgbsv():
    "lub,piv,x,info = sgbsv(kl,ku,ab,b,[overwrite_ab,overwrite_b])\n\nWrapper for ``sgbsv``.\n\nParameters\n----------\nkl : input int\nku : input int\nab : input rank-2 array('f') with bounds (2*kl+ku+1,n)\nb : input rank-2 array('f') with bounds (n,nrhs)\n\nOther Parameters\n----------------\noverwrite_ab : input int, optional\n    Default: 0\noverwrite_b : input int, optional\n    Default: 0\n\nReturns\n-------\nlub : rank-2 array('f') with bounds (2*kl+ku+1,n) and ab storage\npiv : rank-1 array('i') with bounds (n)\nx : rank-2 array('f') with bounds (n,nrhs) and b storage\ninfo : int\n"
    pass

def sgbtrf():
    "lu,ipiv,info = sgbtrf(ab,kl,ku,[m,n,ldab,overwrite_ab])\n\nWrapper for ``sgbtrf``.\n\nParameters\n----------\nab : input rank-2 array('f') with bounds (ldab,*)\nkl : input int\nku : input int\n\nOther Parameters\n----------------\nm : input int, optional\n    Default: shape(ab,1)\nn : input int, optional\n    Default: shape(ab,1)\noverwrite_ab : input int, optional\n    Default: 0\nldab : input int, optional\n    Default: shape(ab,0)\n\nReturns\n-------\nlu : rank-2 array('f') with bounds (ldab,*) and ab storage\nipiv : rank-1 array('i') with bounds (MIN(m,n))\ninfo : int\n"
    pass

def sgbtrs():
    "x,info = sgbtrs(ab,kl,ku,b,ipiv,[trans,n,ldab,ldb,overwrite_b])\n\nWrapper for ``sgbtrs``.\n\nParameters\n----------\nab : input rank-2 array('f') with bounds (ldab,n)\nkl : input int\nku : input int\nb : input rank-2 array('f') with bounds (ldb,nrhs)\nipiv : input rank-1 array('i') with bounds (n)\n\nOther Parameters\n----------------\noverwrite_b : input int, optional\n    Default: 0\ntrans : input int, optional\n    Default: 0\nn : input int, optional\n    Default: shape(ab,1)\nldab : input int, optional\n    Default: shape(ab,0)\nldb : input int, optional\n    Default: shape(b,0)\n\nReturns\n-------\nx : rank-2 array('f') with bounds (ldb,nrhs) and b storage\ninfo : int\n"
    pass

def sgebal():
    "ba,lo,hi,pivscale,info = sgebal(a,[scale,permute,overwrite_a])\n\nWrapper for ``sgebal``.\n\nParameters\n----------\na : input rank-2 array('f') with bounds (m,n)\n\nOther Parameters\n----------------\nscale : input int, optional\n    Default: 0\npermute : input int, optional\n    Default: 0\noverwrite_a : input int, optional\n    Default: 0\n\nReturns\n-------\nba : rank-2 array('f') with bounds (m,n) and a storage\nlo : int\nhi : int\npivscale : rank-1 array('f') with bounds (n)\ninfo : int\n"
    pass

def sgecon():
    "rcond,info = sgecon(a,anorm,[norm])\n\nWrapper for ``sgecon``.\n\nParameters\n----------\na : input rank-2 array('f') with bounds (n,n)\nanorm : input float\n\nOther Parameters\n----------------\nnorm : input string(len=1), optional\n    Default: '1'\n\nReturns\n-------\nrcond : float\ninfo : int\n"
    pass

def sgees():
    "t,sdim,wr,wi,vs,work,info = sgees(sselect,a,[compute_v,sort_t,lwork,sselect_extra_args,overwrite_a])\n\nWrapper for ``sgees``.\n\nParameters\n----------\nsselect : call-back function\na : input rank-2 array('f') with bounds (n,n)\n\nOther Parameters\n----------------\ncompute_v : input int, optional\n    Default: 1\nsort_t : input int, optional\n    Default: 0\nsselect_extra_args : input tuple, optional\n    Default: ()\noverwrite_a : input int, optional\n    Default: 0\nlwork : input int, optional\n    Default: 3*n\n\nReturns\n-------\nt : rank-2 array('f') with bounds (n,n) and a storage\nsdim : int\nwr : rank-1 array('f') with bounds (n)\nwi : rank-1 array('f') with bounds (n)\nvs : rank-2 array('f') with bounds (ldvs,n)\nwork : rank-1 array('f') with bounds (MAX(lwork,1))\ninfo : int\n\nNotes\n-----\nCall-back functions::\n\n  def sselect(arg1,arg2): return sselect\n  Required arguments:\n    arg1 : input float\n    arg2 : input float\n  Return objects:\n    sselect : int\n"
    pass

def sgeev():
    "wr,wi,vl,vr,info = sgeev(a,[compute_vl,compute_vr,lwork,overwrite_a])\n\nWrapper for ``sgeev``.\n\nParameters\n----------\na : input rank-2 array('f') with bounds (n,n)\n\nOther Parameters\n----------------\ncompute_vl : input int, optional\n    Default: 1\ncompute_vr : input int, optional\n    Default: 1\noverwrite_a : input int, optional\n    Default: 0\nlwork : input int, optional\n    Default: 4*n\n\nReturns\n-------\nwr : rank-1 array('f') with bounds (n)\nwi : rank-1 array('f') with bounds (n)\nvl : rank-2 array('f') with bounds (ldvl,n)\nvr : rank-2 array('f') with bounds (ldvr,n)\ninfo : int\n"
    pass

def sgeev_lwork():
    'work,info = sgeev_lwork(n,[compute_vl,compute_vr])\n\nWrapper for ``sgeev_lwork``.\n\nParameters\n----------\nn : input int\n\nOther Parameters\n----------------\ncompute_vl : input int, optional\n    Default: 1\ncompute_vr : input int, optional\n    Default: 1\n\nReturns\n-------\nwork : float\ninfo : int\n'
    pass

def sgegv(*args, **kwds):
    "`sgegv` is deprecated!\nThe `*gegv` family of routines has been deprecated in\nLAPACK 3.6.0 in favor of the `*ggev` family of routines.\nThe corresponding wrappers will be removed from SciPy in\na future release.\n\nalphar,alphai,beta,vl,vr,info = sgegv(a,b,[compute_vl,compute_vr,lwork,overwrite_a,overwrite_b])\n\nWrapper for ``sgegv``.\n\nParameters\n----------\na : input rank-2 array('f') with bounds (n,n)\nb : input rank-2 array('f') with bounds (n,n)\n\nOther Parameters\n----------------\ncompute_vl : input int, optional\n    Default: 1\ncompute_vr : input int, optional\n    Default: 1\noverwrite_a : input int, optional\n    Default: 0\noverwrite_b : input int, optional\n    Default: 0\nlwork : input int, optional\n    Default: 8*n\n\nReturns\n-------\nalphar : rank-1 array('f') with bounds (n)\nalphai : rank-1 array('f') with bounds (n)\nbeta : rank-1 array('f') with bounds (n)\nvl : rank-2 array('f') with bounds (ldvl,n)\nvr : rank-2 array('f') with bounds (ldvr,n)\ninfo : int\n"
    pass

def sgehrd():
    "ht,tau,info = sgehrd(a,[lo,hi,lwork,overwrite_a])\n\nWrapper for ``sgehrd``.\n\nParameters\n----------\na : input rank-2 array('f') with bounds (n,n)\n\nOther Parameters\n----------------\nlo : input int, optional\n    Default: 0\nhi : input int, optional\n    Default: n-1\noverwrite_a : input int, optional\n    Default: 0\nlwork : input int, optional\n    Default: MAX(n,1)\n\nReturns\n-------\nht : rank-2 array('f') with bounds (n,n) and a storage\ntau : rank-1 array('f') with bounds (n - 1)\ninfo : int\n"
    pass

def sgehrd_lwork():
    'work,info = sgehrd_lwork(n,[lo,hi])\n\nWrapper for ``sgehrd_lwork``.\n\nParameters\n----------\nn : input int\n\nOther Parameters\n----------------\nlo : input int, optional\n    Default: 0\nhi : input int, optional\n    Default: n-1\n\nReturns\n-------\nwork : float\ninfo : int\n'
    pass

def sgelsd():
    "x,s,rank,info = sgelsd(a,b,lwork,size_iwork,[cond,overwrite_a,overwrite_b])\n\nWrapper for ``sgelsd``.\n\nParameters\n----------\na : input rank-2 array('f') with bounds (m,n)\nb : input rank-2 array('f') with bounds (maxmn,nrhs)\nlwork : input int\nsize_iwork : input int\n\nOther Parameters\n----------------\noverwrite_a : input int, optional\n    Default: 0\noverwrite_b : input int, optional\n    Default: 0\ncond : input float, optional\n    Default: -1.0\n\nReturns\n-------\nx : rank-2 array('f') with bounds (maxmn,nrhs) and b storage\ns : rank-1 array('f') with bounds (minmn)\nrank : int\ninfo : int\n"
    pass

def sgelsd_lwork():
    'work,iwork,info = sgelsd_lwork(m,n,nrhs,[cond,lwork])\n\nWrapper for ``sgelsd_lwork``.\n\nParameters\n----------\nm : input int\nn : input int\nnrhs : input int\n\nOther Parameters\n----------------\ncond : input float, optional\n    Default: -1.0\nlwork : input int, optional\n    Default: -1\n\nReturns\n-------\nwork : float\niwork : int\ninfo : int\n'
    pass

def sgelss():
    "v,x,s,rank,work,info = sgelss(a,b,[cond,lwork,overwrite_a,overwrite_b])\n\nWrapper for ``sgelss``.\n\nParameters\n----------\na : input rank-2 array('f') with bounds (m,n)\nb : input rank-2 array('f') with bounds (maxmn,nrhs)\n\nOther Parameters\n----------------\noverwrite_a : input int, optional\n    Default: 0\noverwrite_b : input int, optional\n    Default: 0\ncond : input float, optional\n    Default: -1.0\nlwork : input int, optional\n    Default: 3*minmn+MAX(2*minmn,MAX(maxmn,nrhs))\n\nReturns\n-------\nv : rank-2 array('f') with bounds (m,n) and a storage\nx : rank-2 array('f') with bounds (maxmn,nrhs) and b storage\ns : rank-1 array('f') with bounds (minmn)\nrank : int\nwork : rank-1 array('f') with bounds (MAX(lwork,1))\ninfo : int\n"
    pass

def sgelss_lwork():
    'work,info = sgelss_lwork(m,n,nrhs,[cond,lwork])\n\nWrapper for ``sgelss_lwork``.\n\nParameters\n----------\nm : input int\nn : input int\nnrhs : input int\n\nOther Parameters\n----------------\ncond : input float, optional\n    Default: -1.0\nlwork : input int, optional\n    Default: -1\n\nReturns\n-------\nwork : float\ninfo : int\n'
    pass

def sgelsy():
    "v,x,j,rank,info = sgelsy(a,b,jptv,cond,lwork,[overwrite_a,overwrite_b])\n\nWrapper for ``sgelsy``.\n\nParameters\n----------\na : input rank-2 array('f') with bounds (m,n)\nb : input rank-2 array('f') with bounds (maxmn,nrhs)\njptv : input rank-1 array('i') with bounds (n)\ncond : input float\nlwork : input int\n\nOther Parameters\n----------------\noverwrite_a : input int, optional\n    Default: 0\noverwrite_b : input int, optional\n    Default: 0\n\nReturns\n-------\nv : rank-2 array('f') with bounds (m,n) and a storage\nx : rank-2 array('f') with bounds (maxmn,nrhs) and b storage\nj : rank-1 array('i') with bounds (n) and jptv storage\nrank : int\ninfo : int\n"
    pass

def sgelsy_lwork():
    'work,info = sgelsy_lwork(m,n,nrhs,cond,[lwork])\n\nWrapper for ``sgelsy_lwork``.\n\nParameters\n----------\nm : input int\nn : input int\nnrhs : input int\ncond : input float\n\nOther Parameters\n----------------\nlwork : input int, optional\n    Default: -1\n\nReturns\n-------\nwork : float\ninfo : int\n'
    pass

def sgeqp3():
    "qr,jpvt,tau,work,info = sgeqp3(a,[lwork,overwrite_a])\n\nWrapper for ``sgeqp3``.\n\nParameters\n----------\na : input rank-2 array('f') with bounds (m,n)\n\nOther Parameters\n----------------\noverwrite_a : input int, optional\n    Default: 0\nlwork : input int, optional\n    Default: 3*(n+1)\n\nReturns\n-------\nqr : rank-2 array('f') with bounds (m,n) and a storage\njpvt : rank-1 array('i') with bounds (n)\ntau : rank-1 array('f') with bounds (MIN(m,n))\nwork : rank-1 array('f') with bounds (MAX(lwork,1))\ninfo : int\n"
    pass

def sgeqrf():
    "qr,tau,work,info = sgeqrf(a,[lwork,overwrite_a])\n\nWrapper for ``sgeqrf``.\n\nParameters\n----------\na : input rank-2 array('f') with bounds (m,n)\n\nOther Parameters\n----------------\noverwrite_a : input int, optional\n    Default: 0\nlwork : input int, optional\n    Default: 3*n\n\nReturns\n-------\nqr : rank-2 array('f') with bounds (m,n) and a storage\ntau : rank-1 array('f') with bounds (MIN(m,n))\nwork : rank-1 array('f') with bounds (MAX(lwork,1))\ninfo : int\n"
    pass

def sgerqf():
    "qr,tau,work,info = sgerqf(a,[lwork,overwrite_a])\n\nWrapper for ``sgerqf``.\n\nParameters\n----------\na : input rank-2 array('f') with bounds (m,n)\n\nOther Parameters\n----------------\noverwrite_a : input int, optional\n    Default: 0\nlwork : input int, optional\n    Default: 3*m\n\nReturns\n-------\nqr : rank-2 array('f') with bounds (m,n) and a storage\ntau : rank-1 array('f') with bounds (MIN(m,n))\nwork : rank-1 array('f') with bounds (MAX(lwork,1))\ninfo : int\n"
    pass

def sgesdd():
    "u,s,vt,info = sgesdd(a,[compute_uv,full_matrices,lwork,overwrite_a])\n\nWrapper for ``sgesdd``.\n\nParameters\n----------\na : input rank-2 array('f') with bounds (m,n)\n\nOther Parameters\n----------------\noverwrite_a : input int, optional\n    Default: 0\ncompute_uv : input int, optional\n    Default: 1\nfull_matrices : input int, optional\n    Default: 1\nlwork : input int, optional\n    Default: (compute_uv?4*minmn*minmn+MAX(m,n)+9*minmn:MAX(14*minmn+4,10*minmn+2+25*(25+8))+MAX(m,n))\n\nReturns\n-------\nu : rank-2 array('f') with bounds (u0,u1)\ns : rank-1 array('f') with bounds (minmn)\nvt : rank-2 array('f') with bounds (vt0,vt1)\ninfo : int\n"
    pass

def sgesdd_lwork():
    'work,info = sgesdd_lwork(m,n,[compute_uv,full_matrices])\n\nWrapper for ``sgesdd_lwork``.\n\nParameters\n----------\nm : input int\nn : input int\n\nOther Parameters\n----------------\ncompute_uv : input int, optional\n    Default: 1\nfull_matrices : input int, optional\n    Default: 1\n\nReturns\n-------\nwork : float\ninfo : int\n'
    pass

def sgesv():
    "lu,piv,x,info = sgesv(a,b,[overwrite_a,overwrite_b])\n\nWrapper for ``sgesv``.\n\nParameters\n----------\na : input rank-2 array('f') with bounds (n,n)\nb : input rank-2 array('f') with bounds (n,nrhs)\n\nOther Parameters\n----------------\noverwrite_a : input int, optional\n    Default: 0\noverwrite_b : input int, optional\n    Default: 0\n\nReturns\n-------\nlu : rank-2 array('f') with bounds (n,n) and a storage\npiv : rank-1 array('i') with bounds (n)\nx : rank-2 array('f') with bounds (n,nrhs) and b storage\ninfo : int\n"
    pass

def sgesvd():
    "u,s,vt,info = sgesvd(a,[compute_uv,full_matrices,lwork,overwrite_a])\n\nWrapper for ``sgesvd``.\n\nParameters\n----------\na : input rank-2 array('f') with bounds (m,n)\n\nOther Parameters\n----------------\noverwrite_a : input int, optional\n    Default: 0\ncompute_uv : input int, optional\n    Default: 1\nfull_matrices : input int, optional\n    Default: 1\nlwork : input int, optional\n    Default: MAX(1,MAX(3*minmn+MAX(m,n),5*minmn))\n\nReturns\n-------\nu : rank-2 array('f') with bounds (u0,u1)\ns : rank-1 array('f') with bounds (minmn)\nvt : rank-2 array('f') with bounds (vt0,vt1)\ninfo : int\n"
    pass

def sgesvd_lwork():
    'work,info = sgesvd_lwork(m,n,[compute_uv,full_matrices])\n\nWrapper for ``sgesvd_lwork``.\n\nParameters\n----------\nm : input int\nn : input int\n\nOther Parameters\n----------------\ncompute_uv : input int, optional\n    Default: 1\nfull_matrices : input int, optional\n    Default: 1\n\nReturns\n-------\nwork : float\ninfo : int\n'
    pass

def sgesvx():
    "as,lu,ipiv,equed,rs,cs,bs,x,rcond,ferr,berr,info = sgesvx(a,b,[fact,trans,af,ipiv,equed,r,c,overwrite_a,overwrite_b])\n\nWrapper for ``sgesvx``.\n\nParameters\n----------\na : input rank-2 array('f') with bounds (n,n)\nb : input rank-2 array('f') with bounds (n,nrhs)\n\nOther Parameters\n----------------\nfact : input string(len=1), optional\n    Default: 'E'\ntrans : input string(len=1), optional\n    Default: 'N'\noverwrite_a : input int, optional\n    Default: 0\naf : input rank-2 array('f') with bounds (n,n)\nipiv : input rank-1 array('i') with bounds (n)\nequed : input string(len=1), optional\n    Default: 'B'\nr : input rank-1 array('f') with bounds (n)\nc : input rank-1 array('f') with bounds (n)\noverwrite_b : input int, optional\n    Default: 0\n\nReturns\n-------\nas : rank-2 array('f') with bounds (n,n) and a storage\nlu : rank-2 array('f') with bounds (n,n) and af storage\nipiv : rank-1 array('i') with bounds (n)\nequed : string(len=1)\nrs : rank-1 array('f') with bounds (n) and r storage\ncs : rank-1 array('f') with bounds (n) and c storage\nbs : rank-2 array('f') with bounds (n,nrhs) and b storage\nx : rank-2 array('f') with bounds (n,nrhs)\nrcond : float\nferr : rank-1 array('f') with bounds (nrhs)\nberr : rank-1 array('f') with bounds (nrhs)\ninfo : int\n"
    pass

def sgetrf():
    "lu,piv,info = sgetrf(a,[overwrite_a])\n\nWrapper for ``sgetrf``.\n\nParameters\n----------\na : input rank-2 array('f') with bounds (m,n)\n\nOther Parameters\n----------------\noverwrite_a : input int, optional\n    Default: 0\n\nReturns\n-------\nlu : rank-2 array('f') with bounds (m,n) and a storage\npiv : rank-1 array('i') with bounds (MIN(m,n))\ninfo : int\n"
    pass

def sgetri():
    "inv_a,info = sgetri(lu,piv,[lwork,overwrite_lu])\n\nWrapper for ``sgetri``.\n\nParameters\n----------\nlu : input rank-2 array('f') with bounds (n,n)\npiv : input rank-1 array('i') with bounds (n)\n\nOther Parameters\n----------------\noverwrite_lu : input int, optional\n    Default: 0\nlwork : input int, optional\n    Default: 3*n\n\nReturns\n-------\ninv_a : rank-2 array('f') with bounds (n,n) and lu storage\ninfo : int\n"
    pass

def sgetri_lwork():
    'work,info = sgetri_lwork(n)\n\nWrapper for ``sgetri_lwork``.\n\nParameters\n----------\nn : input int\n\nReturns\n-------\nwork : float\ninfo : int\n'
    pass

def sgetrs():
    "x,info = sgetrs(lu,piv,b,[trans,overwrite_b])\n\nWrapper for ``sgetrs``.\n\nParameters\n----------\nlu : input rank-2 array('f') with bounds (n,n)\npiv : input rank-1 array('i') with bounds (n)\nb : input rank-2 array('f') with bounds (n,nrhs)\n\nOther Parameters\n----------------\noverwrite_b : input int, optional\n    Default: 0\ntrans : input int, optional\n    Default: 0\n\nReturns\n-------\nx : rank-2 array('f') with bounds (n,nrhs) and b storage\ninfo : int\n"
    pass

def sgges():
    "a,b,sdim,alphar,alphai,beta,vsl,vsr,work,info = sgges(sselect,a,b,[jobvsl,jobvsr,sort_t,ldvsl,ldvsr,lwork,sselect_extra_args,overwrite_a,overwrite_b])\n\nWrapper for ``sgges``.\n\nParameters\n----------\nsselect : call-back function\na : input rank-2 array('f') with bounds (lda,n)\nb : input rank-2 array('f') with bounds (ldb,n)\n\nOther Parameters\n----------------\njobvsl : input int, optional\n    Default: 1\njobvsr : input int, optional\n    Default: 1\nsort_t : input int, optional\n    Default: 0\nsselect_extra_args : input tuple, optional\n    Default: ()\noverwrite_a : input int, optional\n    Default: 0\noverwrite_b : input int, optional\n    Default: 0\nldvsl : input int, optional\n    Default: ((jobvsl==1)?n:1)\nldvsr : input int, optional\n    Default: ((jobvsr==1)?n:1)\nlwork : input int, optional\n    Default: 8*n+16\n\nReturns\n-------\na : rank-2 array('f') with bounds (lda,n)\nb : rank-2 array('f') with bounds (ldb,n)\nsdim : int\nalphar : rank-1 array('f') with bounds (n)\nalphai : rank-1 array('f') with bounds (n)\nbeta : rank-1 array('f') with bounds (n)\nvsl : rank-2 array('f') with bounds (ldvsl,n)\nvsr : rank-2 array('f') with bounds (ldvsr,n)\nwork : rank-1 array('f') with bounds (MAX(lwork,1))\ninfo : int\n\nNotes\n-----\nCall-back functions::\n\n  def sselect(alphar,alphai,beta): return sselect\n  Required arguments:\n    alphar : input float\n    alphai : input float\n    beta : input float\n  Return objects:\n    sselect : int\n"
    pass

def sggev():
    "alphar,alphai,beta,vl,vr,work,info = sggev(a,b,[compute_vl,compute_vr,lwork,overwrite_a,overwrite_b])\n\nWrapper for ``sggev``.\n\nParameters\n----------\na : input rank-2 array('f') with bounds (n,n)\nb : input rank-2 array('f') with bounds (n,n)\n\nOther Parameters\n----------------\ncompute_vl : input int, optional\n    Default: 1\ncompute_vr : input int, optional\n    Default: 1\noverwrite_a : input int, optional\n    Default: 0\noverwrite_b : input int, optional\n    Default: 0\nlwork : input int, optional\n    Default: 8*n\n\nReturns\n-------\nalphar : rank-1 array('f') with bounds (n)\nalphai : rank-1 array('f') with bounds (n)\nbeta : rank-1 array('f') with bounds (n)\nvl : rank-2 array('f') with bounds (ldvl,n)\nvr : rank-2 array('f') with bounds (ldvr,n)\nwork : rank-1 array('f') with bounds (MAX(lwork,1))\ninfo : int\n"
    pass

def sgtsv():
    "du2,d,du,x,info = sgtsv(dl,d,du,b,[overwrite_dl,overwrite_d,overwrite_du,overwrite_b])\n\nWrapper for ``sgtsv``.\n\nParameters\n----------\ndl : input rank-1 array('f') with bounds (n - 1)\nd : input rank-1 array('f') with bounds (n)\ndu : input rank-1 array('f') with bounds (n - 1)\nb : input rank-2 array('f') with bounds (n,nrhs)\n\nOther Parameters\n----------------\noverwrite_dl : input int, optional\n    Default: 0\noverwrite_d : input int, optional\n    Default: 0\noverwrite_du : input int, optional\n    Default: 0\noverwrite_b : input int, optional\n    Default: 0\n\nReturns\n-------\ndu2 : rank-1 array('f') with bounds (n - 1) and dl storage\nd : rank-1 array('f') with bounds (n)\ndu : rank-1 array('f') with bounds (n - 1)\nx : rank-2 array('f') with bounds (n,nrhs) and b storage\ninfo : int\n"
    pass

def slamch():
    'slamch = slamch(cmach)\n\nWrapper for ``slamch``.\n\nParameters\n----------\ncmach : input string(len=1)\n\nReturns\n-------\nslamch : float\n'
    pass

def slange():
    "n2 = slange(norm,a)\n\nWrapper for ``slange``.\n\nParameters\n----------\nnorm : input string(len=1)\na : input rank-2 array('f') with bounds (m,n)\n\nReturns\n-------\nn2 : float\n"
    pass

def slarf():
    "c = slarf(v,tau,c,work,[side,incv,overwrite_c])\n\nWrapper for ``slarf``.\n\nParameters\n----------\nv : input rank-1 array('f') with bounds (*)\ntau : input float\nc : input rank-2 array('f') with bounds (m,n)\nwork : input rank-1 array('f') with bounds (*)\n\nOther Parameters\n----------------\nside : input string(len=1), optional\n    Default: 'L'\nincv : input int, optional\n    Default: 1\noverwrite_c : input int, optional\n    Default: 0\n\nReturns\n-------\nc : rank-2 array('f') with bounds (m,n)\n"
    pass

def slarfg():
    "alpha,x,tau = slarfg(n,alpha,x,[incx,overwrite_x])\n\nWrapper for ``slarfg``.\n\nParameters\n----------\nn : input int\nalpha : input float\nx : input rank-1 array('f') with bounds (*)\n\nOther Parameters\n----------------\noverwrite_x : input int, optional\n    Default: 0\nincx : input int, optional\n    Default: 1\n\nReturns\n-------\nalpha : float\nx : rank-1 array('f') with bounds (*)\ntau : float\n"
    pass

def slartg():
    'cs,sn,r = slartg(f,g)\n\nWrapper for ``slartg``.\n\nParameters\n----------\nf : input float\ng : input float\n\nReturns\n-------\ncs : float\nsn : float\nr : float\n'
    pass

def slasd4():
    "delta,sigma,work,info = slasd4(i,d,z,[rho])\n\nWrapper for ``slasd4``.\n\nParameters\n----------\ni : input int\nd : input rank-1 array('f') with bounds (n)\nz : input rank-1 array('f') with bounds (n)\n\nOther Parameters\n----------------\nrho : input float, optional\n    Default: 1.0\n\nReturns\n-------\ndelta : rank-1 array('f') with bounds (n)\nsigma : float\nwork : rank-1 array('f') with bounds (n)\ninfo : int\n"
    pass

def slaswp():
    "a = slaswp(a,piv,[k1,k2,off,inc,overwrite_a])\n\nWrapper for ``slaswp``.\n\nParameters\n----------\na : input rank-2 array('f') with bounds (nrows,n)\npiv : input rank-1 array('i') with bounds (*)\n\nOther Parameters\n----------------\noverwrite_a : input int, optional\n    Default: 0\nk1 : input int, optional\n    Default: 0\nk2 : input int, optional\n    Default: len(piv)-1\noff : input int, optional\n    Default: 0\ninc : input int, optional\n    Default: 1\n\nReturns\n-------\na : rank-2 array('f') with bounds (nrows,n)\n"
    pass

def slauum():
    "a,info = slauum(c,[lower,overwrite_c])\n\nWrapper for ``slauum``.\n\nParameters\n----------\nc : input rank-2 array('f') with bounds (n,n)\n\nOther Parameters\n----------------\noverwrite_c : input int, optional\n    Default: 0\nlower : input int, optional\n    Default: 0\n\nReturns\n-------\na : rank-2 array('f') with bounds (n,n) and c storage\ninfo : int\n"
    pass

def sorghr():
    "ht,info = sorghr(a,tau,[lo,hi,lwork,overwrite_a])\n\nWrapper for ``sorghr``.\n\nParameters\n----------\na : input rank-2 array('f') with bounds (n,n)\ntau : input rank-1 array('f') with bounds (n - 1)\n\nOther Parameters\n----------------\nlo : input int, optional\n    Default: 0\nhi : input int, optional\n    Default: n-1\noverwrite_a : input int, optional\n    Default: 0\nlwork : input int, optional\n    Default: hi-lo\n\nReturns\n-------\nht : rank-2 array('f') with bounds (n,n) and a storage\ninfo : int\n"
    pass

def sorghr_lwork():
    'work,info = sorghr_lwork(n,[lo,hi])\n\nWrapper for ``sorghr_lwork``.\n\nParameters\n----------\nn : input int\n\nOther Parameters\n----------------\nlo : input int, optional\n    Default: 0\nhi : input int, optional\n    Default: n-1\n\nReturns\n-------\nwork : float\ninfo : int\n'
    pass

def sorgqr():
    "q,work,info = sorgqr(a,tau,[lwork,overwrite_a])\n\nWrapper for ``sorgqr``.\n\nParameters\n----------\na : input rank-2 array('f') with bounds (m,n)\ntau : input rank-1 array('f') with bounds (k)\n\nOther Parameters\n----------------\noverwrite_a : input int, optional\n    Default: 0\nlwork : input int, optional\n    Default: 3*n\n\nReturns\n-------\nq : rank-2 array('f') with bounds (m,n) and a storage\nwork : rank-1 array('f') with bounds (MAX(lwork,1))\ninfo : int\n"
    pass

def sorgrq():
    "q,work,info = sorgrq(a,tau,[lwork,overwrite_a])\n\nWrapper for ``sorgrq``.\n\nParameters\n----------\na : input rank-2 array('f') with bounds (m,n)\ntau : input rank-1 array('f') with bounds (k)\n\nOther Parameters\n----------------\noverwrite_a : input int, optional\n    Default: 0\nlwork : input int, optional\n    Default: 3*m\n\nReturns\n-------\nq : rank-2 array('f') with bounds (m,n) and a storage\nwork : rank-1 array('f') with bounds (MAX(lwork,1))\ninfo : int\n"
    pass

def sormqr():
    "cq,work,info = sormqr(side,trans,a,tau,c,lwork,[overwrite_c])\n\nWrapper for ``sormqr``.\n\nParameters\n----------\nside : input string(len=1)\ntrans : input string(len=1)\na : input rank-2 array('f') with bounds (lda,k)\ntau : input rank-1 array('f') with bounds (k)\nc : input rank-2 array('f') with bounds (ldc,n)\nlwork : input int\n\nOther Parameters\n----------------\noverwrite_c : input int, optional\n    Default: 0\n\nReturns\n-------\ncq : rank-2 array('f') with bounds (ldc,n) and c storage\nwork : rank-1 array('f') with bounds (MAX(lwork,1))\ninfo : int\n"
    pass

def spbsv():
    "c,x,info = spbsv(ab,b,[lower,ldab,overwrite_ab,overwrite_b])\n\nWrapper for ``spbsv``.\n\nParameters\n----------\nab : input rank-2 array('f') with bounds (ldab,n)\nb : input rank-2 array('f') with bounds (ldb,nrhs)\n\nOther Parameters\n----------------\nlower : input int, optional\n    Default: 0\noverwrite_ab : input int, optional\n    Default: 0\nldab : input int, optional\n    Default: shape(ab,0)\noverwrite_b : input int, optional\n    Default: 0\n\nReturns\n-------\nc : rank-2 array('f') with bounds (ldab,n) and ab storage\nx : rank-2 array('f') with bounds (ldb,nrhs) and b storage\ninfo : int\n"
    pass

def spbtrf():
    "c,info = spbtrf(ab,[lower,ldab,overwrite_ab])\n\nWrapper for ``spbtrf``.\n\nParameters\n----------\nab : input rank-2 array('f') with bounds (ldab,n)\n\nOther Parameters\n----------------\nlower : input int, optional\n    Default: 0\noverwrite_ab : input int, optional\n    Default: 0\nldab : input int, optional\n    Default: shape(ab,0)\n\nReturns\n-------\nc : rank-2 array('f') with bounds (ldab,n) and ab storage\ninfo : int\n"
    pass

def spbtrs():
    "x,info = spbtrs(ab,b,[lower,ldab,overwrite_b])\n\nWrapper for ``spbtrs``.\n\nParameters\n----------\nab : input rank-2 array('f') with bounds (ldab,n)\nb : input rank-2 array('f') with bounds (ldb,nrhs)\n\nOther Parameters\n----------------\nlower : input int, optional\n    Default: 0\nldab : input int, optional\n    Default: shape(ab,0)\noverwrite_b : input int, optional\n    Default: 0\n\nReturns\n-------\nx : rank-2 array('f') with bounds (ldb,nrhs) and b storage\ninfo : int\n"
    pass

def spocon():
    "rcond,info = spocon(a,anorm,[uplo])\n\nWrapper for ``spocon``.\n\nParameters\n----------\na : input rank-2 array('f') with bounds (n,n)\nanorm : input float\n\nOther Parameters\n----------------\nuplo : input string(len=1), optional\n    Default: 'U'\n\nReturns\n-------\nrcond : float\ninfo : int\n"
    pass

def sposv():
    "c,x,info = sposv(a,b,[lower,overwrite_a,overwrite_b])\n\nWrapper for ``sposv``.\n\nParameters\n----------\na : input rank-2 array('f') with bounds (n,n)\nb : input rank-2 array('f') with bounds (n,nrhs)\n\nOther Parameters\n----------------\noverwrite_a : input int, optional\n    Default: 0\noverwrite_b : input int, optional\n    Default: 0\nlower : input int, optional\n    Default: 0\n\nReturns\n-------\nc : rank-2 array('f') with bounds (n,n) and a storage\nx : rank-2 array('f') with bounds (n,nrhs) and b storage\ninfo : int\n"
    pass

def sposvx():
    "a_s,lu,equed,s,b_s,x,rcond,ferr,berr,info = sposvx(a,b,[fact,af,equed,s,lower,overwrite_a,overwrite_b])\n\nWrapper for ``sposvx``.\n\nParameters\n----------\na : input rank-2 array('f') with bounds (n,n)\nb : input rank-2 array('f') with bounds (n,nrhs)\n\nOther Parameters\n----------------\nfact : input string(len=1), optional\n    Default: 'E'\noverwrite_a : input int, optional\n    Default: 0\naf : input rank-2 array('f') with bounds (n,n)\nequed : input string(len=1), optional\n    Default: 'Y'\ns : input rank-1 array('f') with bounds (n)\noverwrite_b : input int, optional\n    Default: 0\nlower : input int, optional\n    Default: 0\n\nReturns\n-------\na_s : rank-2 array('f') with bounds (n,n) and a storage\nlu : rank-2 array('f') with bounds (n,n) and af storage\nequed : string(len=1)\ns : rank-1 array('f') with bounds (n)\nb_s : rank-2 array('f') with bounds (n,nrhs) and b storage\nx : rank-2 array('f') with bounds (n,nrhs)\nrcond : float\nferr : rank-1 array('f') with bounds (nrhs)\nberr : rank-1 array('f') with bounds (nrhs)\ninfo : int\n"
    pass

def spotrf():
    "c,info = spotrf(a,[lower,clean,overwrite_a])\n\nWrapper for ``spotrf``.\n\nParameters\n----------\na : input rank-2 array('f') with bounds (n,n)\n\nOther Parameters\n----------------\noverwrite_a : input int, optional\n    Default: 0\nlower : input int, optional\n    Default: 0\nclean : input int, optional\n    Default: 1\n\nReturns\n-------\nc : rank-2 array('f') with bounds (n,n) and a storage\ninfo : int\n"
    pass

def spotri():
    "inv_a,info = spotri(c,[lower,overwrite_c])\n\nWrapper for ``spotri``.\n\nParameters\n----------\nc : input rank-2 array('f') with bounds (n,n)\n\nOther Parameters\n----------------\noverwrite_c : input int, optional\n    Default: 0\nlower : input int, optional\n    Default: 0\n\nReturns\n-------\ninv_a : rank-2 array('f') with bounds (n,n) and c storage\ninfo : int\n"
    pass

def spotrs():
    "x,info = spotrs(c,b,[lower,overwrite_b])\n\nWrapper for ``spotrs``.\n\nParameters\n----------\nc : input rank-2 array('f') with bounds (n,n)\nb : input rank-2 array('f') with bounds (n,nrhs)\n\nOther Parameters\n----------------\noverwrite_b : input int, optional\n    Default: 0\nlower : input int, optional\n    Default: 0\n\nReturns\n-------\nx : rank-2 array('f') with bounds (n,nrhs) and b storage\ninfo : int\n"
    pass

def sptsv():
    "d,du,x,info = sptsv(d,e,b,[overwrite_d,overwrite_e,overwrite_b])\n\nWrapper for ``sptsv``.\n\nParameters\n----------\nd : input rank-1 array('f') with bounds (n)\ne : input rank-1 array('f') with bounds (n - 1)\nb : input rank-2 array('f') with bounds (n,nrhs)\n\nOther Parameters\n----------------\noverwrite_d : input int, optional\n    Default: 0\noverwrite_e : input int, optional\n    Default: 0\noverwrite_b : input int, optional\n    Default: 0\n\nReturns\n-------\nd : rank-1 array('f') with bounds (n)\ndu : rank-1 array('f') with bounds (n - 1) and e storage\nx : rank-2 array('f') with bounds (n,nrhs) and b storage\ninfo : int\n"
    pass

def ssbev():
    "w,z,info = ssbev(ab,[compute_v,lower,ldab,overwrite_ab])\n\nWrapper for ``ssbev``.\n\nParameters\n----------\nab : input rank-2 array('f') with bounds (ldab,n)\n\nOther Parameters\n----------------\noverwrite_ab : input int, optional\n    Default: 1\ncompute_v : input int, optional\n    Default: 1\nlower : input int, optional\n    Default: 0\nldab : input int, optional\n    Default: shape(ab,0)\n\nReturns\n-------\nw : rank-1 array('f') with bounds (n)\nz : rank-2 array('f') with bounds (ldz,ldz)\ninfo : int\n"
    pass

def ssbevd():
    "w,z,info = ssbevd(ab,[compute_v,lower,ldab,liwork,overwrite_ab])\n\nWrapper for ``ssbevd``.\n\nParameters\n----------\nab : input rank-2 array('f') with bounds (ldab,n)\n\nOther Parameters\n----------------\noverwrite_ab : input int, optional\n    Default: 1\ncompute_v : input int, optional\n    Default: 1\nlower : input int, optional\n    Default: 0\nldab : input int, optional\n    Default: shape(ab,0)\nliwork : input int, optional\n    Default: (compute_v?3+5*n:1)\n\nReturns\n-------\nw : rank-1 array('f') with bounds (n)\nz : rank-2 array('f') with bounds (ldz,ldz)\ninfo : int\n"
    pass

def ssbevx():
    "w,z,m,ifail,info = ssbevx(ab,vl,vu,il,iu,[ldab,compute_v,range,lower,abstol,mmax,overwrite_ab])\n\nWrapper for ``ssbevx``.\n\nParameters\n----------\nab : input rank-2 array('f') with bounds (ldab,n)\nvl : input float\nvu : input float\nil : input int\niu : input int\n\nOther Parameters\n----------------\noverwrite_ab : input int, optional\n    Default: 1\nldab : input int, optional\n    Default: shape(ab,0)\ncompute_v : input int, optional\n    Default: 1\nrange : input int, optional\n    Default: 0\nlower : input int, optional\n    Default: 0\nabstol : input float, optional\n    Default: 0.0\nmmax : input int, optional\n    Default: (compute_v?(range==2?(iu-il+1):n):1)\n\nReturns\n-------\nw : rank-1 array('f') with bounds (n)\nz : rank-2 array('f') with bounds (ldz,mmax)\nm : int\nifail : rank-1 array('i') with bounds ((compute_v?n:1))\ninfo : int\n"
    pass

def ssyev():
    "w,v,info = ssyev(a,[compute_v,lower,lwork,overwrite_a])\n\nWrapper for ``ssyev``.\n\nParameters\n----------\na : input rank-2 array('f') with bounds (n,n)\n\nOther Parameters\n----------------\ncompute_v : input int, optional\n    Default: 1\nlower : input int, optional\n    Default: 0\noverwrite_a : input int, optional\n    Default: 0\nlwork : input int, optional\n    Default: 3*n-1\n\nReturns\n-------\nw : rank-1 array('f') with bounds (n)\nv : rank-2 array('f') with bounds (n,n) and a storage\ninfo : int\n"
    pass

def ssyevd():
    "w,v,info = ssyevd(a,[compute_v,lower,lwork,overwrite_a])\n\nWrapper for ``ssyevd``.\n\nParameters\n----------\na : input rank-2 array('f') with bounds (n,n)\n\nOther Parameters\n----------------\ncompute_v : input int, optional\n    Default: 1\nlower : input int, optional\n    Default: 0\noverwrite_a : input int, optional\n    Default: 0\nlwork : input int, optional\n    Default: (compute_v?1+6*n+2*n*n:2*n+1)\n\nReturns\n-------\nw : rank-1 array('f') with bounds (n)\nv : rank-2 array('f') with bounds (n,n) and a storage\ninfo : int\n"
    pass

def ssyevr():
    "w,z,info = ssyevr(a,[jobz,range,uplo,il,iu,lwork,overwrite_a])\n\nWrapper for ``ssyevr``.\n\nParameters\n----------\na : input rank-2 array('f') with bounds (n,n)\n\nOther Parameters\n----------------\njobz : input string(len=1), optional\n    Default: 'V'\nrange : input string(len=1), optional\n    Default: 'A'\nuplo : input string(len=1), optional\n    Default: 'L'\noverwrite_a : input int, optional\n    Default: 0\nil : input int, optional\n    Default: 1\niu : input int, optional\n    Default: n\nlwork : input int, optional\n    Default: 26*n\n\nReturns\n-------\nw : rank-1 array('f') with bounds (n)\nz : rank-2 array('f') with bounds (n,m)\ninfo : int\n"
    pass

def ssygv():
    "a,w,info = ssygv(a,b,[itype,jobz,uplo,overwrite_a,overwrite_b])\n\nWrapper for ``ssygv``.\n\nParameters\n----------\na : input rank-2 array('f') with bounds (n,n)\nb : input rank-2 array('f') with bounds (n,n)\n\nOther Parameters\n----------------\nitype : input int, optional\n    Default: 1\njobz : input string(len=1), optional\n    Default: 'V'\nuplo : input string(len=1), optional\n    Default: 'L'\noverwrite_a : input int, optional\n    Default: 0\noverwrite_b : input int, optional\n    Default: 0\n\nReturns\n-------\na : rank-2 array('f') with bounds (n,n)\nw : rank-1 array('f') with bounds (n)\ninfo : int\n"
    pass

def ssygvd():
    "a,w,info = ssygvd(a,b,[itype,jobz,uplo,lwork,overwrite_a,overwrite_b])\n\nWrapper for ``ssygvd``.\n\nParameters\n----------\na : input rank-2 array('f') with bounds (n,n)\nb : input rank-2 array('f') with bounds (n,n)\n\nOther Parameters\n----------------\nitype : input int, optional\n    Default: 1\njobz : input string(len=1), optional\n    Default: 'V'\nuplo : input string(len=1), optional\n    Default: 'L'\noverwrite_a : input int, optional\n    Default: 0\noverwrite_b : input int, optional\n    Default: 0\nlwork : input int, optional\n    Default: 1+6*n+2*n*n\n\nReturns\n-------\na : rank-2 array('f') with bounds (n,n)\nw : rank-1 array('f') with bounds (n)\ninfo : int\n"
    pass

def ssygvx():
    "w,z,ifail,info = ssygvx(a,b,iu,[itype,jobz,uplo,il,lwork,overwrite_a,overwrite_b])\n\nWrapper for ``ssygvx``.\n\nParameters\n----------\na : input rank-2 array('f') with bounds (n,n)\nb : input rank-2 array('f') with bounds (n,n)\niu : input int\n\nOther Parameters\n----------------\nitype : input int, optional\n    Default: 1\njobz : input string(len=1), optional\n    Default: 'V'\nuplo : input string(len=1), optional\n    Default: 'L'\noverwrite_a : input int, optional\n    Default: 0\noverwrite_b : input int, optional\n    Default: 0\nil : input int, optional\n    Default: 1\nlwork : input int, optional\n    Default: 8*n\n\nReturns\n-------\nw : rank-1 array('f') with bounds (n)\nz : rank-2 array('f') with bounds (n,m)\nifail : rank-1 array('i') with bounds (n)\ninfo : int\n"
    pass

def ssysv():
    "udut,ipiv,x,info = ssysv(a,b,[lwork,lower,overwrite_a,overwrite_b])\n\nWrapper for ``ssysv``.\n\nParameters\n----------\na : input rank-2 array('f') with bounds (n,n)\nb : input rank-2 array('f') with bounds (n,nrhs)\n\nOther Parameters\n----------------\noverwrite_a : input int, optional\n    Default: 0\noverwrite_b : input int, optional\n    Default: 0\nlwork : input int, optional\n    Default: n\nlower : input int, optional\n    Default: 0\n\nReturns\n-------\nudut : rank-2 array('f') with bounds (n,n) and a storage\nipiv : rank-1 array('i') with bounds (n)\nx : rank-2 array('f') with bounds (n,nrhs) and b storage\ninfo : int\n"
    pass

def ssysv_lwork():
    'work,info = ssysv_lwork(n,[lower])\n\nWrapper for ``ssysv_lwork``.\n\nParameters\n----------\nn : input int\n\nOther Parameters\n----------------\nlower : input int, optional\n    Default: 0\n\nReturns\n-------\nwork : float\ninfo : int\n'
    pass

def ssysvx():
    "a_s,udut,ipiv,b_s,x,rcond,ferr,berr,info = ssysvx(a,b,[af,ipiv,lwork,factored,lower,overwrite_a,overwrite_b])\n\nWrapper for ``ssysvx``.\n\nParameters\n----------\na : input rank-2 array('f') with bounds (n,n)\nb : input rank-2 array('f') with bounds (n,nrhs)\n\nOther Parameters\n----------------\noverwrite_a : input int, optional\n    Default: 0\naf : input rank-2 array('f') with bounds (n,n)\nipiv : input rank-1 array('i') with bounds (n)\noverwrite_b : input int, optional\n    Default: 0\nlwork : input int, optional\n    Default: 3*n\nfactored : input int, optional\n    Default: 0\nlower : input int, optional\n    Default: 0\n\nReturns\n-------\na_s : rank-2 array('f') with bounds (n,n) and a storage\nudut : rank-2 array('f') with bounds (n,n) and af storage\nipiv : rank-1 array('i') with bounds (n)\nb_s : rank-2 array('f') with bounds (n,nrhs) and b storage\nx : rank-2 array('f') with bounds (n,nrhs)\nrcond : float\nferr : rank-1 array('f') with bounds (nrhs)\nberr : rank-1 array('f') with bounds (nrhs)\ninfo : int\n"
    pass

def ssysvx_lwork():
    'work,info = ssysvx_lwork(n,[lower])\n\nWrapper for ``ssysvx_lwork``.\n\nParameters\n----------\nn : input int\n\nOther Parameters\n----------------\nlower : input int, optional\n    Default: 0\n\nReturns\n-------\nwork : float\ninfo : int\n'
    pass

def stgsen():
    "a,b,alphar,alphai,beta,q,z,m,pl,pr,dif,work,iwork,info = stgsen(select,a,b,q,z,[lwork,liwork,overwrite_a,overwrite_b,overwrite_q,overwrite_z])\n\nWrapper for ``stgsen``.\n\nParameters\n----------\nselect : input rank-1 array('i') with bounds (n)\na : input rank-2 array('f') with bounds (lda,n)\nb : input rank-2 array('f') with bounds (ldb,n)\nq : input rank-2 array('f') with bounds (ldq,n)\nz : input rank-2 array('f') with bounds (ldz,n)\n\nOther Parameters\n----------------\noverwrite_a : input int, optional\n    Default: 0\noverwrite_b : input int, optional\n    Default: 0\noverwrite_q : input int, optional\n    Default: 0\noverwrite_z : input int, optional\n    Default: 0\nlwork : input int, optional\n    Default: MAX(4*n+16,2*m*(n-m))\nliwork : input int, optional\n    Default: n+6\n\nReturns\n-------\na : rank-2 array('f') with bounds (lda,n)\nb : rank-2 array('f') with bounds (ldb,n)\nalphar : rank-1 array('f') with bounds (n)\nalphai : rank-1 array('f') with bounds (n)\nbeta : rank-1 array('f') with bounds (n)\nq : rank-2 array('f') with bounds (ldq,n)\nz : rank-2 array('f') with bounds (ldz,n)\nm : int\npl : float\npr : float\ndif : rank-1 array('f') with bounds (2)\nwork : rank-1 array('f') with bounds (MAX(lwork,1))\niwork : rank-1 array('i') with bounds (MAX(1,liwork))\ninfo : int\n"
    pass

def strsyl():
    "x,scale,info = strsyl(a,b,c,[trana,tranb,isgn,overwrite_c])\n\nWrapper for ``strsyl``.\n\nParameters\n----------\na : input rank-2 array('f') with bounds (m,m)\nb : input rank-2 array('f') with bounds (n,n)\nc : input rank-2 array('f') with bounds (m,n)\n\nOther Parameters\n----------------\ntrana : input string(len=1), optional\n    Default: 'N'\ntranb : input string(len=1), optional\n    Default: 'N'\nisgn : input int, optional\n    Default: 1\noverwrite_c : input int, optional\n    Default: 0\n\nReturns\n-------\nx : rank-2 array('f') with bounds (m,n) and c storage\nscale : float\ninfo : int\n"
    pass

def strtri():
    "inv_c,info = strtri(c,[lower,unitdiag,overwrite_c])\n\nWrapper for ``strtri``.\n\nParameters\n----------\nc : input rank-2 array('f') with bounds (n,n)\n\nOther Parameters\n----------------\noverwrite_c : input int, optional\n    Default: 0\nlower : input int, optional\n    Default: 0\nunitdiag : input int, optional\n    Default: 0\n\nReturns\n-------\ninv_c : rank-2 array('f') with bounds (n,n) and c storage\ninfo : int\n"
    pass

def strtrs():
    "x,info = strtrs(a,b,[lower,trans,unitdiag,lda,overwrite_b])\n\nWrapper for ``strtrs``.\n\nParameters\n----------\na : input rank-2 array('f') with bounds (lda,n)\nb : input rank-2 array('f') with bounds (ldb,nrhs)\n\nOther Parameters\n----------------\nlower : input int, optional\n    Default: 0\ntrans : input int, optional\n    Default: 0\nunitdiag : input int, optional\n    Default: 0\nlda : input int, optional\n    Default: shape(a,0)\noverwrite_b : input int, optional\n    Default: 0\n\nReturns\n-------\nx : rank-2 array('f') with bounds (ldb,nrhs) and b storage\ninfo : int\n"
    pass

def zgbsv():
    "lub,piv,x,info = zgbsv(kl,ku,ab,b,[overwrite_ab,overwrite_b])\n\nWrapper for ``zgbsv``.\n\nParameters\n----------\nkl : input int\nku : input int\nab : input rank-2 array('D') with bounds (2*kl+ku+1,n)\nb : input rank-2 array('D') with bounds (n,nrhs)\n\nOther Parameters\n----------------\noverwrite_ab : input int, optional\n    Default: 0\noverwrite_b : input int, optional\n    Default: 0\n\nReturns\n-------\nlub : rank-2 array('D') with bounds (2*kl+ku+1,n) and ab storage\npiv : rank-1 array('i') with bounds (n)\nx : rank-2 array('D') with bounds (n,nrhs) and b storage\ninfo : int\n"
    pass

def zgbtrf():
    "lu,ipiv,info = zgbtrf(ab,kl,ku,[m,n,ldab,overwrite_ab])\n\nWrapper for ``zgbtrf``.\n\nParameters\n----------\nab : input rank-2 array('D') with bounds (ldab,*)\nkl : input int\nku : input int\n\nOther Parameters\n----------------\nm : input int, optional\n    Default: shape(ab,1)\nn : input int, optional\n    Default: shape(ab,1)\noverwrite_ab : input int, optional\n    Default: 0\nldab : input int, optional\n    Default: shape(ab,0)\n\nReturns\n-------\nlu : rank-2 array('D') with bounds (ldab,*) and ab storage\nipiv : rank-1 array('i') with bounds (MIN(m,n))\ninfo : int\n"
    pass

def zgbtrs():
    "x,info = zgbtrs(ab,kl,ku,b,ipiv,[trans,n,ldab,ldb,overwrite_b])\n\nWrapper for ``zgbtrs``.\n\nParameters\n----------\nab : input rank-2 array('D') with bounds (ldab,n)\nkl : input int\nku : input int\nb : input rank-2 array('D') with bounds (ldb,nrhs)\nipiv : input rank-1 array('i') with bounds (n)\n\nOther Parameters\n----------------\noverwrite_b : input int, optional\n    Default: 0\ntrans : input int, optional\n    Default: 0\nn : input int, optional\n    Default: shape(ab,1)\nldab : input int, optional\n    Default: shape(ab,0)\nldb : input int, optional\n    Default: shape(b,0)\n\nReturns\n-------\nx : rank-2 array('D') with bounds (ldb,nrhs) and b storage\ninfo : int\n"
    pass

def zgebal():
    "ba,lo,hi,pivscale,info = zgebal(a,[scale,permute,overwrite_a])\n\nWrapper for ``zgebal``.\n\nParameters\n----------\na : input rank-2 array('D') with bounds (m,n)\n\nOther Parameters\n----------------\nscale : input int, optional\n    Default: 0\npermute : input int, optional\n    Default: 0\noverwrite_a : input int, optional\n    Default: 0\n\nReturns\n-------\nba : rank-2 array('D') with bounds (m,n) and a storage\nlo : int\nhi : int\npivscale : rank-1 array('d') with bounds (n)\ninfo : int\n"
    pass

def zgecon():
    "rcond,info = zgecon(a,anorm,[norm])\n\nWrapper for ``zgecon``.\n\nParameters\n----------\na : input rank-2 array('D') with bounds (n,n)\nanorm : input float\n\nOther Parameters\n----------------\nnorm : input string(len=1), optional\n    Default: '1'\n\nReturns\n-------\nrcond : float\ninfo : int\n"
    pass

def zgees():
    "t,sdim,w,vs,work,info = zgees(zselect,a,[compute_v,sort_t,lwork,zselect_extra_args,overwrite_a])\n\nWrapper for ``zgees``.\n\nParameters\n----------\nzselect : call-back function\na : input rank-2 array('D') with bounds (n,n)\n\nOther Parameters\n----------------\ncompute_v : input int, optional\n    Default: 1\nsort_t : input int, optional\n    Default: 0\nzselect_extra_args : input tuple, optional\n    Default: ()\noverwrite_a : input int, optional\n    Default: 0\nlwork : input int, optional\n    Default: 3*n\n\nReturns\n-------\nt : rank-2 array('D') with bounds (n,n) and a storage\nsdim : int\nw : rank-1 array('D') with bounds (n)\nvs : rank-2 array('D') with bounds (ldvs,n)\nwork : rank-1 array('D') with bounds (MAX(lwork,1))\ninfo : int\n\nNotes\n-----\nCall-back functions::\n\n  def zselect(arg): return zselect\n  Required arguments:\n    arg : input complex\n  Return objects:\n    zselect : int\n"
    pass

def zgeev():
    "w,vl,vr,info = zgeev(a,[compute_vl,compute_vr,lwork,overwrite_a])\n\nWrapper for ``zgeev``.\n\nParameters\n----------\na : input rank-2 array('D') with bounds (n,n)\n\nOther Parameters\n----------------\ncompute_vl : input int, optional\n    Default: 1\ncompute_vr : input int, optional\n    Default: 1\noverwrite_a : input int, optional\n    Default: 0\nlwork : input int, optional\n    Default: 2*n\n\nReturns\n-------\nw : rank-1 array('D') with bounds (n)\nvl : rank-2 array('D') with bounds (ldvl,n)\nvr : rank-2 array('D') with bounds (ldvr,n)\ninfo : int\n"
    pass

def zgeev_lwork():
    'work,info = zgeev_lwork(n,[compute_vl,compute_vr])\n\nWrapper for ``zgeev_lwork``.\n\nParameters\n----------\nn : input int\n\nOther Parameters\n----------------\ncompute_vl : input int, optional\n    Default: 1\ncompute_vr : input int, optional\n    Default: 1\n\nReturns\n-------\nwork : complex\ninfo : int\n'
    pass

def zgegv(*args, **kwds):
    "`zgegv` is deprecated!\nThe `*gegv` family of routines has been deprecated in\nLAPACK 3.6.0 in favor of the `*ggev` family of routines.\nThe corresponding wrappers will be removed from SciPy in\na future release.\n\nalpha,beta,vl,vr,info = zgegv(a,b,[compute_vl,compute_vr,lwork,overwrite_a,overwrite_b])\n\nWrapper for ``zgegv``.\n\nParameters\n----------\na : input rank-2 array('D') with bounds (n,n)\nb : input rank-2 array('D') with bounds (n,n)\n\nOther Parameters\n----------------\ncompute_vl : input int, optional\n    Default: 1\ncompute_vr : input int, optional\n    Default: 1\noverwrite_a : input int, optional\n    Default: 0\noverwrite_b : input int, optional\n    Default: 0\nlwork : input int, optional\n    Default: 2*n\n\nReturns\n-------\nalpha : rank-1 array('D') with bounds (n)\nbeta : rank-1 array('D') with bounds (n)\nvl : rank-2 array('D') with bounds (ldvl,n)\nvr : rank-2 array('D') with bounds (ldvr,n)\ninfo : int\n"
    pass

def zgehrd():
    "ht,tau,info = zgehrd(a,[lo,hi,lwork,overwrite_a])\n\nWrapper for ``zgehrd``.\n\nParameters\n----------\na : input rank-2 array('D') with bounds (n,n)\n\nOther Parameters\n----------------\nlo : input int, optional\n    Default: 0\nhi : input int, optional\n    Default: n-1\noverwrite_a : input int, optional\n    Default: 0\nlwork : input int, optional\n    Default: MAX(n,1)\n\nReturns\n-------\nht : rank-2 array('D') with bounds (n,n) and a storage\ntau : rank-1 array('D') with bounds (n - 1)\ninfo : int\n"
    pass

def zgehrd_lwork():
    'work,info = zgehrd_lwork(n,[lo,hi])\n\nWrapper for ``zgehrd_lwork``.\n\nParameters\n----------\nn : input int\n\nOther Parameters\n----------------\nlo : input int, optional\n    Default: 0\nhi : input int, optional\n    Default: n-1\n\nReturns\n-------\nwork : complex\ninfo : int\n'
    pass

def zgelsd():
    "x,s,rank,info = zgelsd(a,b,lwork,size_rwork,size_iwork,[cond,overwrite_a,overwrite_b])\n\nWrapper for ``zgelsd``.\n\nParameters\n----------\na : input rank-2 array('D') with bounds (m,n)\nb : input rank-2 array('D') with bounds (maxmn,nrhs)\nlwork : input int\nsize_rwork : input int\nsize_iwork : input int\n\nOther Parameters\n----------------\noverwrite_a : input int, optional\n    Default: 0\noverwrite_b : input int, optional\n    Default: 0\ncond : input float, optional\n    Default: -1.0\n\nReturns\n-------\nx : rank-2 array('D') with bounds (maxmn,nrhs) and b storage\ns : rank-1 array('d') with bounds (minmn)\nrank : int\ninfo : int\n"
    pass

def zgelsd_lwork():
    'work,rwork,iwork,info = zgelsd_lwork(m,n,nrhs,[cond,lwork])\n\nWrapper for ``zgelsd_lwork``.\n\nParameters\n----------\nm : input int\nn : input int\nnrhs : input int\n\nOther Parameters\n----------------\ncond : input float, optional\n    Default: -1.0\nlwork : input int, optional\n    Default: -1\n\nReturns\n-------\nwork : complex\nrwork : float\niwork : int\ninfo : int\n'
    pass

def zgelss():
    "v,x,s,rank,work,info = zgelss(a,b,[cond,lwork,overwrite_a,overwrite_b])\n\nWrapper for ``zgelss``.\n\nParameters\n----------\na : input rank-2 array('D') with bounds (m,n)\nb : input rank-2 array('D') with bounds (maxmn,nrhs)\n\nOther Parameters\n----------------\noverwrite_a : input int, optional\n    Default: 0\noverwrite_b : input int, optional\n    Default: 0\ncond : input float, optional\n    Default: -1.0\nlwork : input int, optional\n    Default: 2*minmn+MAX(maxmn,nrhs)\n\nReturns\n-------\nv : rank-2 array('D') with bounds (m,n) and a storage\nx : rank-2 array('D') with bounds (maxmn,nrhs) and b storage\ns : rank-1 array('d') with bounds (minmn)\nrank : int\nwork : rank-1 array('D') with bounds (MAX(lwork,1))\ninfo : int\n"
    pass

def zgelss_lwork():
    'work,info = zgelss_lwork(m,n,nrhs,[cond,lwork])\n\nWrapper for ``zgelss_lwork``.\n\nParameters\n----------\nm : input int\nn : input int\nnrhs : input int\n\nOther Parameters\n----------------\ncond : input float, optional\n    Default: -1.0\nlwork : input int, optional\n    Default: -1\n\nReturns\n-------\nwork : complex\ninfo : int\n'
    pass

def zgelsy():
    "v,x,j,rank,info = zgelsy(a,b,jptv,cond,lwork,[overwrite_a,overwrite_b])\n\nWrapper for ``zgelsy``.\n\nParameters\n----------\na : input rank-2 array('D') with bounds (m,n)\nb : input rank-2 array('D') with bounds (maxmn,nrhs)\njptv : input rank-1 array('i') with bounds (n)\ncond : input float\nlwork : input int\n\nOther Parameters\n----------------\noverwrite_a : input int, optional\n    Default: 0\noverwrite_b : input int, optional\n    Default: 0\n\nReturns\n-------\nv : rank-2 array('D') with bounds (m,n) and a storage\nx : rank-2 array('D') with bounds (maxmn,nrhs) and b storage\nj : rank-1 array('i') with bounds (n) and jptv storage\nrank : int\ninfo : int\n"
    pass

def zgelsy_lwork():
    'work,info = zgelsy_lwork(m,n,nrhs,cond,[lwork])\n\nWrapper for ``zgelsy_lwork``.\n\nParameters\n----------\nm : input int\nn : input int\nnrhs : input int\ncond : input float\n\nOther Parameters\n----------------\nlwork : input int, optional\n    Default: -1\n\nReturns\n-------\nwork : complex\ninfo : int\n'
    pass

def zgeqp3():
    "qr,jpvt,tau,work,info = zgeqp3(a,[lwork,overwrite_a])\n\nWrapper for ``zgeqp3``.\n\nParameters\n----------\na : input rank-2 array('D') with bounds (m,n)\n\nOther Parameters\n----------------\noverwrite_a : input int, optional\n    Default: 0\nlwork : input int, optional\n    Default: 3*(n+1)\n\nReturns\n-------\nqr : rank-2 array('D') with bounds (m,n) and a storage\njpvt : rank-1 array('i') with bounds (n)\ntau : rank-1 array('D') with bounds (MIN(m,n))\nwork : rank-1 array('D') with bounds (MAX(lwork,1))\ninfo : int\n"
    pass

def zgeqrf():
    "qr,tau,work,info = zgeqrf(a,[lwork,overwrite_a])\n\nWrapper for ``zgeqrf``.\n\nParameters\n----------\na : input rank-2 array('D') with bounds (m,n)\n\nOther Parameters\n----------------\noverwrite_a : input int, optional\n    Default: 0\nlwork : input int, optional\n    Default: 3*n\n\nReturns\n-------\nqr : rank-2 array('D') with bounds (m,n) and a storage\ntau : rank-1 array('D') with bounds (MIN(m,n))\nwork : rank-1 array('D') with bounds (MAX(lwork,1))\ninfo : int\n"
    pass

def zgerqf():
    "qr,tau,work,info = zgerqf(a,[lwork,overwrite_a])\n\nWrapper for ``zgerqf``.\n\nParameters\n----------\na : input rank-2 array('D') with bounds (m,n)\n\nOther Parameters\n----------------\noverwrite_a : input int, optional\n    Default: 0\nlwork : input int, optional\n    Default: 3*m\n\nReturns\n-------\nqr : rank-2 array('D') with bounds (m,n) and a storage\ntau : rank-1 array('D') with bounds (MIN(m,n))\nwork : rank-1 array('D') with bounds (MAX(lwork,1))\ninfo : int\n"
    pass

def zgesdd():
    "u,s,vt,info = zgesdd(a,[compute_uv,full_matrices,lwork,overwrite_a])\n\nWrapper for ``zgesdd``.\n\nParameters\n----------\na : input rank-2 array('D') with bounds (m,n)\n\nOther Parameters\n----------------\noverwrite_a : input int, optional\n    Default: 0\ncompute_uv : input int, optional\n    Default: 1\nfull_matrices : input int, optional\n    Default: 1\nlwork : input int, optional\n    Default: (compute_uv?2*minmn*minmn+MAX(m,n)+2*minmn:2*minmn+MAX(m,n))\n\nReturns\n-------\nu : rank-2 array('D') with bounds (u0,u1)\ns : rank-1 array('d') with bounds (minmn)\nvt : rank-2 array('D') with bounds (vt0,vt1)\ninfo : int\n"
    pass

def zgesdd_lwork():
    'work,info = zgesdd_lwork(m,n,[compute_uv,full_matrices])\n\nWrapper for ``zgesdd_lwork``.\n\nParameters\n----------\nm : input int\nn : input int\n\nOther Parameters\n----------------\ncompute_uv : input int, optional\n    Default: 1\nfull_matrices : input int, optional\n    Default: 1\n\nReturns\n-------\nwork : complex\ninfo : int\n'
    pass

def zgesv():
    "lu,piv,x,info = zgesv(a,b,[overwrite_a,overwrite_b])\n\nWrapper for ``zgesv``.\n\nParameters\n----------\na : input rank-2 array('D') with bounds (n,n)\nb : input rank-2 array('D') with bounds (n,nrhs)\n\nOther Parameters\n----------------\noverwrite_a : input int, optional\n    Default: 0\noverwrite_b : input int, optional\n    Default: 0\n\nReturns\n-------\nlu : rank-2 array('D') with bounds (n,n) and a storage\npiv : rank-1 array('i') with bounds (n)\nx : rank-2 array('D') with bounds (n,nrhs) and b storage\ninfo : int\n"
    pass

def zgesvd():
    "u,s,vt,info = zgesvd(a,[compute_uv,full_matrices,lwork,overwrite_a])\n\nWrapper for ``zgesvd``.\n\nParameters\n----------\na : input rank-2 array('D') with bounds (m,n)\n\nOther Parameters\n----------------\noverwrite_a : input int, optional\n    Default: 0\ncompute_uv : input int, optional\n    Default: 1\nfull_matrices : input int, optional\n    Default: 1\nlwork : input int, optional\n    Default: MAX(1,2*minmn+MAX(m,n))\n\nReturns\n-------\nu : rank-2 array('D') with bounds (u0,u1)\ns : rank-1 array('d') with bounds (minmn)\nvt : rank-2 array('D') with bounds (vt0,vt1)\ninfo : int\n"
    pass

def zgesvd_lwork():
    'work,info = zgesvd_lwork(m,n,[compute_uv,full_matrices])\n\nWrapper for ``zgesvd_lwork``.\n\nParameters\n----------\nm : input int\nn : input int\n\nOther Parameters\n----------------\ncompute_uv : input int, optional\n    Default: 1\nfull_matrices : input int, optional\n    Default: 1\n\nReturns\n-------\nwork : complex\ninfo : int\n'
    pass

def zgesvx():
    "as,lu,ipiv,equed,rs,cs,bs,x,rcond,ferr,berr,info = zgesvx(a,b,[fact,trans,af,ipiv,equed,r,c,overwrite_a,overwrite_b])\n\nWrapper for ``zgesvx``.\n\nParameters\n----------\na : input rank-2 array('D') with bounds (n,n)\nb : input rank-2 array('D') with bounds (n,nrhs)\n\nOther Parameters\n----------------\nfact : input string(len=1), optional\n    Default: 'E'\ntrans : input string(len=1), optional\n    Default: 'N'\noverwrite_a : input int, optional\n    Default: 0\naf : input rank-2 array('D') with bounds (n,n)\nipiv : input rank-1 array('i') with bounds (n)\nequed : input string(len=1), optional\n    Default: 'B'\nr : input rank-1 array('d') with bounds (n)\nc : input rank-1 array('d') with bounds (n)\noverwrite_b : input int, optional\n    Default: 0\n\nReturns\n-------\nas : rank-2 array('D') with bounds (n,n) and a storage\nlu : rank-2 array('D') with bounds (n,n) and af storage\nipiv : rank-1 array('i') with bounds (n)\nequed : string(len=1)\nrs : rank-1 array('d') with bounds (n) and r storage\ncs : rank-1 array('d') with bounds (n) and c storage\nbs : rank-2 array('D') with bounds (n,nrhs) and b storage\nx : rank-2 array('D') with bounds (n,nrhs)\nrcond : float\nferr : rank-1 array('d') with bounds (nrhs)\nberr : rank-1 array('d') with bounds (nrhs)\ninfo : int\n"
    pass

def zgetrf():
    "lu,piv,info = zgetrf(a,[overwrite_a])\n\nWrapper for ``zgetrf``.\n\nParameters\n----------\na : input rank-2 array('D') with bounds (m,n)\n\nOther Parameters\n----------------\noverwrite_a : input int, optional\n    Default: 0\n\nReturns\n-------\nlu : rank-2 array('D') with bounds (m,n) and a storage\npiv : rank-1 array('i') with bounds (MIN(m,n))\ninfo : int\n"
    pass

def zgetri():
    "inv_a,info = zgetri(lu,piv,[lwork,overwrite_lu])\n\nWrapper for ``zgetri``.\n\nParameters\n----------\nlu : input rank-2 array('D') with bounds (n,n)\npiv : input rank-1 array('i') with bounds (n)\n\nOther Parameters\n----------------\noverwrite_lu : input int, optional\n    Default: 0\nlwork : input int, optional\n    Default: 3*n\n\nReturns\n-------\ninv_a : rank-2 array('D') with bounds (n,n) and lu storage\ninfo : int\n"
    pass

def zgetri_lwork():
    'work,info = zgetri_lwork(n)\n\nWrapper for ``zgetri_lwork``.\n\nParameters\n----------\nn : input int\n\nReturns\n-------\nwork : complex\ninfo : int\n'
    pass

def zgetrs():
    "x,info = zgetrs(lu,piv,b,[trans,overwrite_b])\n\nWrapper for ``zgetrs``.\n\nParameters\n----------\nlu : input rank-2 array('D') with bounds (n,n)\npiv : input rank-1 array('i') with bounds (n)\nb : input rank-2 array('D') with bounds (n,nrhs)\n\nOther Parameters\n----------------\noverwrite_b : input int, optional\n    Default: 0\ntrans : input int, optional\n    Default: 0\n\nReturns\n-------\nx : rank-2 array('D') with bounds (n,nrhs) and b storage\ninfo : int\n"
    pass

def zgges():
    "a,b,sdim,alpha,beta,vsl,vsr,work,info = zgges(zselect,a,b,[jobvsl,jobvsr,sort_t,ldvsl,ldvsr,lwork,zselect_extra_args,overwrite_a,overwrite_b])\n\nWrapper for ``zgges``.\n\nParameters\n----------\nzselect : call-back function\na : input rank-2 array('D') with bounds (lda,n)\nb : input rank-2 array('D') with bounds (ldb,n)\n\nOther Parameters\n----------------\njobvsl : input int, optional\n    Default: 1\njobvsr : input int, optional\n    Default: 1\nsort_t : input int, optional\n    Default: 0\nzselect_extra_args : input tuple, optional\n    Default: ()\noverwrite_a : input int, optional\n    Default: 0\noverwrite_b : input int, optional\n    Default: 0\nldvsl : input int, optional\n    Default: ((jobvsl==1)?n:1)\nldvsr : input int, optional\n    Default: ((jobvsr==1)?n:1)\nlwork : input int, optional\n    Default: 2*n\n\nReturns\n-------\na : rank-2 array('D') with bounds (lda,n)\nb : rank-2 array('D') with bounds (ldb,n)\nsdim : int\nalpha : rank-1 array('D') with bounds (n)\nbeta : rank-1 array('D') with bounds (n)\nvsl : rank-2 array('D') with bounds (ldvsl,n)\nvsr : rank-2 array('D') with bounds (ldvsr,n)\nwork : rank-1 array('D') with bounds (MAX(lwork,1))\ninfo : int\n\nNotes\n-----\nCall-back functions::\n\n  def zselect(alpha,beta): return zselect\n  Required arguments:\n    alpha : input complex\n    beta : input complex\n  Return objects:\n    zselect : int\n"
    pass

def zggev():
    "alpha,beta,vl,vr,work,info = zggev(a,b,[compute_vl,compute_vr,lwork,overwrite_a,overwrite_b])\n\nWrapper for ``zggev``.\n\nParameters\n----------\na : input rank-2 array('D') with bounds (n,n)\nb : input rank-2 array('D') with bounds (n,n)\n\nOther Parameters\n----------------\ncompute_vl : input int, optional\n    Default: 1\ncompute_vr : input int, optional\n    Default: 1\noverwrite_a : input int, optional\n    Default: 0\noverwrite_b : input int, optional\n    Default: 0\nlwork : input int, optional\n    Default: 2*n\n\nReturns\n-------\nalpha : rank-1 array('D') with bounds (n)\nbeta : rank-1 array('D') with bounds (n)\nvl : rank-2 array('D') with bounds (ldvl,n)\nvr : rank-2 array('D') with bounds (ldvr,n)\nwork : rank-1 array('D') with bounds (MAX(lwork,1))\ninfo : int\n"
    pass

def zgtsv():
    "du2,d,du,x,info = zgtsv(dl,d,du,b,[overwrite_dl,overwrite_d,overwrite_du,overwrite_b])\n\nWrapper for ``zgtsv``.\n\nParameters\n----------\ndl : input rank-1 array('D') with bounds (n - 1)\nd : input rank-1 array('D') with bounds (n)\ndu : input rank-1 array('D') with bounds (n - 1)\nb : input rank-2 array('D') with bounds (n,nrhs)\n\nOther Parameters\n----------------\noverwrite_dl : input int, optional\n    Default: 0\noverwrite_d : input int, optional\n    Default: 0\noverwrite_du : input int, optional\n    Default: 0\noverwrite_b : input int, optional\n    Default: 0\n\nReturns\n-------\ndu2 : rank-1 array('D') with bounds (n - 1) and dl storage\nd : rank-1 array('D') with bounds (n)\ndu : rank-1 array('D') with bounds (n - 1)\nx : rank-2 array('D') with bounds (n,nrhs) and b storage\ninfo : int\n"
    pass

def zhbevd():
    "w,z,info = zhbevd(ab,[compute_v,lower,ldab,lrwork,liwork,overwrite_ab])\n\nWrapper for ``zhbevd``.\n\nParameters\n----------\nab : input rank-2 array('D') with bounds (ldab,n)\n\nOther Parameters\n----------------\noverwrite_ab : input int, optional\n    Default: 1\ncompute_v : input int, optional\n    Default: 1\nlower : input int, optional\n    Default: 0\nldab : input int, optional\n    Default: shape(ab,0)\nlrwork : input int, optional\n    Default: (compute_v?1+5*n+2*n*n:n)\nliwork : input int, optional\n    Default: (compute_v?3+5*n:1)\n\nReturns\n-------\nw : rank-1 array('d') with bounds (n)\nz : rank-2 array('D') with bounds (ldz,ldz)\ninfo : int\n"
    pass

def zhbevx():
    "w,z,m,ifail,info = zhbevx(ab,vl,vu,il,iu,[ldab,compute_v,range,lower,abstol,mmax,overwrite_ab])\n\nWrapper for ``zhbevx``.\n\nParameters\n----------\nab : input rank-2 array('D') with bounds (ldab,n)\nvl : input float\nvu : input float\nil : input int\niu : input int\n\nOther Parameters\n----------------\noverwrite_ab : input int, optional\n    Default: 1\nldab : input int, optional\n    Default: shape(ab,0)\ncompute_v : input int, optional\n    Default: 1\nrange : input int, optional\n    Default: 0\nlower : input int, optional\n    Default: 0\nabstol : input float, optional\n    Default: 0.0\nmmax : input int, optional\n    Default: (compute_v?(range==2?(iu-il+1):n):1)\n\nReturns\n-------\nw : rank-1 array('d') with bounds (n)\nz : rank-2 array('D') with bounds (ldz,mmax)\nm : int\nifail : rank-1 array('i') with bounds ((compute_v?n:1))\ninfo : int\n"
    pass

def zheev():
    "w,v,info = zheev(a,[compute_v,lower,lwork,overwrite_a])\n\nWrapper for ``zheev``.\n\nParameters\n----------\na : input rank-2 array('D') with bounds (n,n)\n\nOther Parameters\n----------------\ncompute_v : input int, optional\n    Default: 1\nlower : input int, optional\n    Default: 0\noverwrite_a : input int, optional\n    Default: 0\nlwork : input int, optional\n    Default: 2*n-1\n\nReturns\n-------\nw : rank-1 array('d') with bounds (n)\nv : rank-2 array('D') with bounds (n,n) and a storage\ninfo : int\n"
    pass

def zheevd():
    "w,v,info = zheevd(a,[compute_v,lower,lwork,overwrite_a])\n\nWrapper for ``zheevd``.\n\nParameters\n----------\na : input rank-2 array('D') with bounds (n,n)\n\nOther Parameters\n----------------\ncompute_v : input int, optional\n    Default: 1\nlower : input int, optional\n    Default: 0\noverwrite_a : input int, optional\n    Default: 0\nlwork : input int, optional\n    Default: (compute_v?2*n+n*n:n+1)\n\nReturns\n-------\nw : rank-1 array('d') with bounds (n)\nv : rank-2 array('D') with bounds (n,n) and a storage\ninfo : int\n"
    pass

def zheevr():
    "w,z,info = zheevr(a,[jobz,range,uplo,il,iu,lwork,overwrite_a])\n\nWrapper for ``zheevr``.\n\nParameters\n----------\na : input rank-2 array('D') with bounds (n,n)\n\nOther Parameters\n----------------\njobz : input string(len=1), optional\n    Default: 'V'\nrange : input string(len=1), optional\n    Default: 'A'\nuplo : input string(len=1), optional\n    Default: 'L'\noverwrite_a : input int, optional\n    Default: 0\nil : input int, optional\n    Default: 1\niu : input int, optional\n    Default: n\nlwork : input int, optional\n    Default: 18*n\n\nReturns\n-------\nw : rank-1 array('d') with bounds (n)\nz : rank-2 array('D') with bounds (n,m)\ninfo : int\n"
    pass

def zhegv():
    "a,w,info = zhegv(a,b,[itype,jobz,uplo,overwrite_a,overwrite_b])\n\nWrapper for ``zhegv``.\n\nParameters\n----------\na : input rank-2 array('D') with bounds (n,n)\nb : input rank-2 array('D') with bounds (n,n)\n\nOther Parameters\n----------------\nitype : input int, optional\n    Default: 1\njobz : input string(len=1), optional\n    Default: 'V'\nuplo : input string(len=1), optional\n    Default: 'L'\noverwrite_a : input int, optional\n    Default: 0\noverwrite_b : input int, optional\n    Default: 0\n\nReturns\n-------\na : rank-2 array('D') with bounds (n,n)\nw : rank-1 array('d') with bounds (n)\ninfo : int\n"
    pass

def zhegvd():
    "a,w,info = zhegvd(a,b,[itype,jobz,uplo,lwork,overwrite_a,overwrite_b])\n\nWrapper for ``zhegvd``.\n\nParameters\n----------\na : input rank-2 array('D') with bounds (n,n)\nb : input rank-2 array('D') with bounds (n,n)\n\nOther Parameters\n----------------\nitype : input int, optional\n    Default: 1\njobz : input string(len=1), optional\n    Default: 'V'\nuplo : input string(len=1), optional\n    Default: 'L'\noverwrite_a : input int, optional\n    Default: 0\noverwrite_b : input int, optional\n    Default: 0\nlwork : input int, optional\n    Default: 2*n+n*n\n\nReturns\n-------\na : rank-2 array('D') with bounds (n,n)\nw : rank-1 array('d') with bounds (n)\ninfo : int\n"
    pass

def zhegvx():
    "w,z,ifail,info = zhegvx(a,b,iu,[itype,jobz,uplo,il,lwork,overwrite_a,overwrite_b])\n\nWrapper for ``zhegvx``.\n\nParameters\n----------\na : input rank-2 array('D') with bounds (n,n)\nb : input rank-2 array('D') with bounds (n,n)\niu : input int\n\nOther Parameters\n----------------\nitype : input int, optional\n    Default: 1\njobz : input string(len=1), optional\n    Default: 'V'\nuplo : input string(len=1), optional\n    Default: 'L'\noverwrite_a : input int, optional\n    Default: 0\noverwrite_b : input int, optional\n    Default: 0\nil : input int, optional\n    Default: 1\nlwork : input int, optional\n    Default: 18*n-1\n\nReturns\n-------\nw : rank-1 array('d') with bounds (n)\nz : rank-2 array('D') with bounds (n,m)\nifail : rank-1 array('i') with bounds (n)\ninfo : int\n"
    pass

def zhesv():
    "uduh,ipiv,x,info = zhesv(a,b,[lwork,lower,overwrite_a,overwrite_b])\n\nWrapper for ``zhesv``.\n\nParameters\n----------\na : input rank-2 array('D') with bounds (n,n)\nb : input rank-2 array('D') with bounds (n,nrhs)\n\nOther Parameters\n----------------\noverwrite_a : input int, optional\n    Default: 0\noverwrite_b : input int, optional\n    Default: 0\nlwork : input int, optional\n    Default: n\nlower : input int, optional\n    Default: 0\n\nReturns\n-------\nuduh : rank-2 array('D') with bounds (n,n) and a storage\nipiv : rank-1 array('i') with bounds (n)\nx : rank-2 array('D') with bounds (n,nrhs) and b storage\ninfo : int\n"
    pass

def zhesv_lwork():
    'work,info = zhesv_lwork(n,[lower])\n\nWrapper for ``zhesv_lwork``.\n\nParameters\n----------\nn : input int\n\nOther Parameters\n----------------\nlower : input int, optional\n    Default: 0\n\nReturns\n-------\nwork : complex\ninfo : int\n'
    pass

def zhesvx():
    "uduh,ipiv,x,rcond,ferr,berr,info = zhesvx(a,b,[af,ipiv,lwork,factored,lower,overwrite_a,overwrite_b])\n\nWrapper for ``zhesvx``.\n\nParameters\n----------\na : input rank-2 array('D') with bounds (n,n)\nb : input rank-2 array('D') with bounds (n,nrhs)\n\nOther Parameters\n----------------\noverwrite_a : input int, optional\n    Default: 0\naf : input rank-2 array('D') with bounds (n,n)\nipiv : input rank-1 array('i') with bounds (n)\noverwrite_b : input int, optional\n    Default: 0\nlwork : input int, optional\n    Default: 2*n\nfactored : input int, optional\n    Default: 0\nlower : input int, optional\n    Default: 0\n\nReturns\n-------\nuduh : rank-2 array('D') with bounds (n,n) and af storage\nipiv : rank-1 array('i') with bounds (n)\nx : rank-2 array('D') with bounds (n,nrhs)\nrcond : float\nferr : rank-1 array('d') with bounds (nrhs)\nberr : rank-1 array('d') with bounds (nrhs)\ninfo : int\n"
    pass

def zhesvx_lwork():
    'work,info = zhesvx_lwork(n,[lower])\n\nWrapper for ``zhesvx_lwork``.\n\nParameters\n----------\nn : input int\n\nOther Parameters\n----------------\nlower : input int, optional\n    Default: 0\n\nReturns\n-------\nwork : complex\ninfo : int\n'
    pass

def zlange():
    "n2 = zlange(norm,a)\n\nWrapper for ``zlange``.\n\nParameters\n----------\nnorm : input string(len=1)\na : input rank-2 array('D') with bounds (m,n)\n\nReturns\n-------\nn2 : float\n"
    pass

def zlarf():
    "c = zlarf(v,tau,c,work,[side,incv,overwrite_c])\n\nWrapper for ``zlarf``.\n\nParameters\n----------\nv : input rank-1 array('D') with bounds (*)\ntau : input complex\nc : input rank-2 array('D') with bounds (m,n)\nwork : input rank-1 array('D') with bounds (*)\n\nOther Parameters\n----------------\nside : input string(len=1), optional\n    Default: 'L'\nincv : input int, optional\n    Default: 1\noverwrite_c : input int, optional\n    Default: 0\n\nReturns\n-------\nc : rank-2 array('D') with bounds (m,n)\n"
    pass

def zlarfg():
    "alpha,x,tau = zlarfg(n,alpha,x,[incx,overwrite_x])\n\nWrapper for ``zlarfg``.\n\nParameters\n----------\nn : input int\nalpha : input complex\nx : input rank-1 array('D') with bounds (*)\n\nOther Parameters\n----------------\noverwrite_x : input int, optional\n    Default: 0\nincx : input int, optional\n    Default: 1\n\nReturns\n-------\nalpha : complex\nx : rank-1 array('D') with bounds (*)\ntau : complex\n"
    pass

def zlartg():
    'cs,sn,r = zlartg(f,g)\n\nWrapper for ``zlartg``.\n\nParameters\n----------\nf : input complex\ng : input complex\n\nReturns\n-------\ncs : float\nsn : complex\nr : complex\n'
    pass

def zlaswp():
    "a = zlaswp(a,piv,[k1,k2,off,inc,overwrite_a])\n\nWrapper for ``zlaswp``.\n\nParameters\n----------\na : input rank-2 array('D') with bounds (nrows,n)\npiv : input rank-1 array('i') with bounds (*)\n\nOther Parameters\n----------------\noverwrite_a : input int, optional\n    Default: 0\nk1 : input int, optional\n    Default: 0\nk2 : input int, optional\n    Default: len(piv)-1\noff : input int, optional\n    Default: 0\ninc : input int, optional\n    Default: 1\n\nReturns\n-------\na : rank-2 array('D') with bounds (nrows,n)\n"
    pass

def zlauum():
    "a,info = zlauum(c,[lower,overwrite_c])\n\nWrapper for ``zlauum``.\n\nParameters\n----------\nc : input rank-2 array('D') with bounds (n,n)\n\nOther Parameters\n----------------\noverwrite_c : input int, optional\n    Default: 0\nlower : input int, optional\n    Default: 0\n\nReturns\n-------\na : rank-2 array('D') with bounds (n,n) and c storage\ninfo : int\n"
    pass

def zpbsv():
    "c,x,info = zpbsv(ab,b,[lower,ldab,overwrite_ab,overwrite_b])\n\nWrapper for ``zpbsv``.\n\nParameters\n----------\nab : input rank-2 array('D') with bounds (ldab,n)\nb : input rank-2 array('D') with bounds (ldb,nrhs)\n\nOther Parameters\n----------------\nlower : input int, optional\n    Default: 0\noverwrite_ab : input int, optional\n    Default: 0\nldab : input int, optional\n    Default: shape(ab,0)\noverwrite_b : input int, optional\n    Default: 0\n\nReturns\n-------\nc : rank-2 array('D') with bounds (ldab,n) and ab storage\nx : rank-2 array('D') with bounds (ldb,nrhs) and b storage\ninfo : int\n"
    pass

def zpbtrf():
    "c,info = zpbtrf(ab,[lower,ldab,overwrite_ab])\n\nWrapper for ``zpbtrf``.\n\nParameters\n----------\nab : input rank-2 array('D') with bounds (ldab,n)\n\nOther Parameters\n----------------\nlower : input int, optional\n    Default: 0\noverwrite_ab : input int, optional\n    Default: 0\nldab : input int, optional\n    Default: shape(ab,0)\n\nReturns\n-------\nc : rank-2 array('D') with bounds (ldab,n) and ab storage\ninfo : int\n"
    pass

def zpbtrs():
    "x,info = zpbtrs(ab,b,[lower,ldab,overwrite_b])\n\nWrapper for ``zpbtrs``.\n\nParameters\n----------\nab : input rank-2 array('D') with bounds (ldab,n)\nb : input rank-2 array('D') with bounds (ldb,nrhs)\n\nOther Parameters\n----------------\nlower : input int, optional\n    Default: 0\nldab : input int, optional\n    Default: shape(ab,0)\noverwrite_b : input int, optional\n    Default: 0\n\nReturns\n-------\nx : rank-2 array('D') with bounds (ldb,nrhs) and b storage\ninfo : int\n"
    pass

def zpocon():
    "rcond,info = zpocon(a,anorm,[uplo])\n\nWrapper for ``zpocon``.\n\nParameters\n----------\na : input rank-2 array('D') with bounds (n,n)\nanorm : input float\n\nOther Parameters\n----------------\nuplo : input string(len=1), optional\n    Default: 'U'\n\nReturns\n-------\nrcond : float\ninfo : int\n"
    pass

def zposv():
    "c,x,info = zposv(a,b,[lower,overwrite_a,overwrite_b])\n\nWrapper for ``zposv``.\n\nParameters\n----------\na : input rank-2 array('D') with bounds (n,n)\nb : input rank-2 array('D') with bounds (n,nrhs)\n\nOther Parameters\n----------------\noverwrite_a : input int, optional\n    Default: 0\noverwrite_b : input int, optional\n    Default: 0\nlower : input int, optional\n    Default: 0\n\nReturns\n-------\nc : rank-2 array('D') with bounds (n,n) and a storage\nx : rank-2 array('D') with bounds (n,nrhs) and b storage\ninfo : int\n"
    pass

def zposvx():
    "a_s,lu,equed,s,b_s,x,rcond,ferr,berr,info = zposvx(a,b,[fact,af,equed,s,lower,overwrite_a,overwrite_b])\n\nWrapper for ``zposvx``.\n\nParameters\n----------\na : input rank-2 array('D') with bounds (n,n)\nb : input rank-2 array('D') with bounds (n,nrhs)\n\nOther Parameters\n----------------\nfact : input string(len=1), optional\n    Default: 'E'\noverwrite_a : input int, optional\n    Default: 0\naf : input rank-2 array('D') with bounds (n,n)\nequed : input string(len=1), optional\n    Default: 'Y'\ns : input rank-1 array('d') with bounds (n)\noverwrite_b : input int, optional\n    Default: 0\nlower : input int, optional\n    Default: 0\n\nReturns\n-------\na_s : rank-2 array('D') with bounds (n,n) and a storage\nlu : rank-2 array('D') with bounds (n,n) and af storage\nequed : string(len=1)\ns : rank-1 array('d') with bounds (n)\nb_s : rank-2 array('D') with bounds (n,nrhs) and b storage\nx : rank-2 array('D') with bounds (n,nrhs)\nrcond : float\nferr : rank-1 array('d') with bounds (nrhs)\nberr : rank-1 array('d') with bounds (nrhs)\ninfo : int\n"
    pass

def zpotrf():
    "c,info = zpotrf(a,[lower,clean,overwrite_a])\n\nWrapper for ``zpotrf``.\n\nParameters\n----------\na : input rank-2 array('D') with bounds (n,n)\n\nOther Parameters\n----------------\noverwrite_a : input int, optional\n    Default: 0\nlower : input int, optional\n    Default: 0\nclean : input int, optional\n    Default: 1\n\nReturns\n-------\nc : rank-2 array('D') with bounds (n,n) and a storage\ninfo : int\n"
    pass

def zpotri():
    "inv_a,info = zpotri(c,[lower,overwrite_c])\n\nWrapper for ``zpotri``.\n\nParameters\n----------\nc : input rank-2 array('D') with bounds (n,n)\n\nOther Parameters\n----------------\noverwrite_c : input int, optional\n    Default: 0\nlower : input int, optional\n    Default: 0\n\nReturns\n-------\ninv_a : rank-2 array('D') with bounds (n,n) and c storage\ninfo : int\n"
    pass

def zpotrs():
    "x,info = zpotrs(c,b,[lower,overwrite_b])\n\nWrapper for ``zpotrs``.\n\nParameters\n----------\nc : input rank-2 array('D') with bounds (n,n)\nb : input rank-2 array('D') with bounds (n,nrhs)\n\nOther Parameters\n----------------\noverwrite_b : input int, optional\n    Default: 0\nlower : input int, optional\n    Default: 0\n\nReturns\n-------\nx : rank-2 array('D') with bounds (n,nrhs) and b storage\ninfo : int\n"
    pass

def zptsv():
    "d,du,x,info = zptsv(d,e,b,[overwrite_d,overwrite_e,overwrite_b])\n\nWrapper for ``zptsv``.\n\nParameters\n----------\nd : input rank-1 array('d') with bounds (n)\ne : input rank-1 array('D') with bounds (n - 1)\nb : input rank-2 array('D') with bounds (n,nrhs)\n\nOther Parameters\n----------------\noverwrite_d : input int, optional\n    Default: 0\noverwrite_e : input int, optional\n    Default: 0\noverwrite_b : input int, optional\n    Default: 0\n\nReturns\n-------\nd : rank-1 array('d') with bounds (n)\ndu : rank-1 array('D') with bounds (n - 1) and e storage\nx : rank-2 array('D') with bounds (n,nrhs) and b storage\ninfo : int\n"
    pass

def zrot():
    "x,y = zrot(x,y,c,s,[n,offx,incx,offy,incy,overwrite_x,overwrite_y])\n\nWrapper for ``zrot``.\n\nParameters\n----------\nx : input rank-1 array('D') with bounds (*)\ny : input rank-1 array('D') with bounds (*)\nc : input float\ns : input complex\n\nOther Parameters\n----------------\nn : input int, optional\n    Default: (len(x)-1-offx)/abs(incx)+1\noverwrite_x : input int, optional\n    Default: 0\noffx : input int, optional\n    Default: 0\nincx : input int, optional\n    Default: 1\noverwrite_y : input int, optional\n    Default: 0\noffy : input int, optional\n    Default: 0\nincy : input int, optional\n    Default: 1\n\nReturns\n-------\nx : rank-1 array('D') with bounds (*)\ny : rank-1 array('D') with bounds (*)\n"
    pass

def zsysv():
    "udut,ipiv,x,info = zsysv(a,b,[lwork,lower,overwrite_a,overwrite_b])\n\nWrapper for ``zsysv``.\n\nParameters\n----------\na : input rank-2 array('D') with bounds (n,n)\nb : input rank-2 array('D') with bounds (n,nrhs)\n\nOther Parameters\n----------------\noverwrite_a : input int, optional\n    Default: 0\noverwrite_b : input int, optional\n    Default: 0\nlwork : input int, optional\n    Default: n\nlower : input int, optional\n    Default: 0\n\nReturns\n-------\nudut : rank-2 array('D') with bounds (n,n) and a storage\nipiv : rank-1 array('i') with bounds (n)\nx : rank-2 array('D') with bounds (n,nrhs) and b storage\ninfo : int\n"
    pass

def zsysv_lwork():
    'work,info = zsysv_lwork(n,[lower])\n\nWrapper for ``zsysv_lwork``.\n\nParameters\n----------\nn : input int\n\nOther Parameters\n----------------\nlower : input int, optional\n    Default: 0\n\nReturns\n-------\nwork : complex\ninfo : int\n'
    pass

def zsysvx():
    "a_s,udut,ipiv,b_s,x,rcond,ferr,berr,info = zsysvx(a,b,[af,ipiv,lwork,factored,lower,overwrite_a,overwrite_b])\n\nWrapper for ``zsysvx``.\n\nParameters\n----------\na : input rank-2 array('D') with bounds (n,n)\nb : input rank-2 array('D') with bounds (n,nrhs)\n\nOther Parameters\n----------------\noverwrite_a : input int, optional\n    Default: 0\naf : input rank-2 array('D') with bounds (n,n)\nipiv : input rank-1 array('i') with bounds (n)\noverwrite_b : input int, optional\n    Default: 0\nlwork : input int, optional\n    Default: 3*n\nfactored : input int, optional\n    Default: 0\nlower : input int, optional\n    Default: 0\n\nReturns\n-------\na_s : rank-2 array('D') with bounds (n,n) and a storage\nudut : rank-2 array('D') with bounds (n,n) and af storage\nipiv : rank-1 array('i') with bounds (n)\nb_s : rank-2 array('D') with bounds (n,nrhs) and b storage\nx : rank-2 array('D') with bounds (n,nrhs)\nrcond : float\nferr : rank-1 array('d') with bounds (nrhs)\nberr : rank-1 array('d') with bounds (nrhs)\ninfo : int\n"
    pass

def zsysvx_lwork():
    'work,info = zsysvx_lwork(n,[lower])\n\nWrapper for ``zsysvx_lwork``.\n\nParameters\n----------\nn : input int\n\nOther Parameters\n----------------\nlower : input int, optional\n    Default: 0\n\nReturns\n-------\nwork : complex\ninfo : int\n'
    pass

def ztgsen():
    "a,b,alpha,beta,q,z,m,pl,pr,dif,work,iwork,info = ztgsen(select,a,b,q,z,[lwork,liwork,overwrite_a,overwrite_b,overwrite_q,overwrite_z])\n\nWrapper for ``ztgsen``.\n\nParameters\n----------\nselect : input rank-1 array('i') with bounds (n)\na : input rank-2 array('D') with bounds (lda,n)\nb : input rank-2 array('D') with bounds (ldb,n)\nq : input rank-2 array('D') with bounds (ldq,n)\nz : input rank-2 array('D') with bounds (ldz,n)\n\nOther Parameters\n----------------\noverwrite_a : input int, optional\n    Default: 0\noverwrite_b : input int, optional\n    Default: 0\noverwrite_q : input int, optional\n    Default: 0\noverwrite_z : input int, optional\n    Default: 0\nlwork : input int, optional\n    Default: 2*m*(n-m)\nliwork : input int, optional\n    Default: n+2\n\nReturns\n-------\na : rank-2 array('D') with bounds (lda,n)\nb : rank-2 array('D') with bounds (ldb,n)\nalpha : rank-1 array('D') with bounds (n)\nbeta : rank-1 array('D') with bounds (n)\nq : rank-2 array('D') with bounds (ldq,n)\nz : rank-2 array('D') with bounds (ldz,n)\nm : int\npl : float\npr : float\ndif : rank-1 array('d') with bounds (2)\nwork : rank-1 array('D') with bounds (MAX(lwork,1))\niwork : rank-1 array('i') with bounds (MAX(1,liwork))\ninfo : int\n"
    pass

def ztrsyl():
    "x,scale,info = ztrsyl(a,b,c,[trana,tranb,isgn,overwrite_c])\n\nWrapper for ``ztrsyl``.\n\nParameters\n----------\na : input rank-2 array('D') with bounds (m,m)\nb : input rank-2 array('D') with bounds (n,n)\nc : input rank-2 array('D') with bounds (m,n)\n\nOther Parameters\n----------------\ntrana : input string(len=1), optional\n    Default: 'N'\ntranb : input string(len=1), optional\n    Default: 'N'\nisgn : input int, optional\n    Default: 1\noverwrite_c : input int, optional\n    Default: 0\n\nReturns\n-------\nx : rank-2 array('D') with bounds (m,n) and c storage\nscale : float\ninfo : int\n"
    pass

def ztrtri():
    "inv_c,info = ztrtri(c,[lower,unitdiag,overwrite_c])\n\nWrapper for ``ztrtri``.\n\nParameters\n----------\nc : input rank-2 array('D') with bounds (n,n)\n\nOther Parameters\n----------------\noverwrite_c : input int, optional\n    Default: 0\nlower : input int, optional\n    Default: 0\nunitdiag : input int, optional\n    Default: 0\n\nReturns\n-------\ninv_c : rank-2 array('D') with bounds (n,n) and c storage\ninfo : int\n"
    pass

def ztrtrs():
    "x,info = ztrtrs(a,b,[lower,trans,unitdiag,lda,overwrite_b])\n\nWrapper for ``ztrtrs``.\n\nParameters\n----------\na : input rank-2 array('D') with bounds (lda,n)\nb : input rank-2 array('D') with bounds (ldb,nrhs)\n\nOther Parameters\n----------------\nlower : input int, optional\n    Default: 0\ntrans : input int, optional\n    Default: 0\nunitdiag : input int, optional\n    Default: 0\nlda : input int, optional\n    Default: shape(a,0)\noverwrite_b : input int, optional\n    Default: 0\n\nReturns\n-------\nx : rank-2 array('D') with bounds (ldb,nrhs) and b storage\ninfo : int\n"
    pass

def zunghr():
    "ht,info = zunghr(a,tau,[lo,hi,lwork,overwrite_a])\n\nWrapper for ``zunghr``.\n\nParameters\n----------\na : input rank-2 array('D') with bounds (n,n)\ntau : input rank-1 array('D') with bounds (n - 1)\n\nOther Parameters\n----------------\nlo : input int, optional\n    Default: 0\nhi : input int, optional\n    Default: n-1\noverwrite_a : input int, optional\n    Default: 0\nlwork : input int, optional\n    Default: hi-lo\n\nReturns\n-------\nht : rank-2 array('D') with bounds (n,n) and a storage\ninfo : int\n"
    pass

def zunghr_lwork():
    'work,info = zunghr_lwork(n,[lo,hi])\n\nWrapper for ``zunghr_lwork``.\n\nParameters\n----------\nn : input int\n\nOther Parameters\n----------------\nlo : input int, optional\n    Default: 0\nhi : input int, optional\n    Default: n-1\n\nReturns\n-------\nwork : complex\ninfo : int\n'
    pass

def zungqr():
    "q,work,info = zungqr(a,tau,[lwork,overwrite_a])\n\nWrapper for ``zungqr``.\n\nParameters\n----------\na : input rank-2 array('D') with bounds (m,n)\ntau : input rank-1 array('D') with bounds (k)\n\nOther Parameters\n----------------\noverwrite_a : input int, optional\n    Default: 0\nlwork : input int, optional\n    Default: 3*n\n\nReturns\n-------\nq : rank-2 array('D') with bounds (m,n) and a storage\nwork : rank-1 array('D') with bounds (MAX(lwork,1))\ninfo : int\n"
    pass

def zungrq():
    "q,work,info = zungrq(a,tau,[lwork,overwrite_a])\n\nWrapper for ``zungrq``.\n\nParameters\n----------\na : input rank-2 array('D') with bounds (m,n)\ntau : input rank-1 array('D') with bounds (k)\n\nOther Parameters\n----------------\noverwrite_a : input int, optional\n    Default: 0\nlwork : input int, optional\n    Default: 3*m\n\nReturns\n-------\nq : rank-2 array('D') with bounds (m,n) and a storage\nwork : rank-1 array('D') with bounds (MAX(lwork,1))\ninfo : int\n"
    pass

def zunmqr():
    "cq,work,info = zunmqr(side,trans,a,tau,c,lwork,[overwrite_c])\n\nWrapper for ``zunmqr``.\n\nParameters\n----------\nside : input string(len=1)\ntrans : input string(len=1)\na : input rank-2 array('D') with bounds (lda,k)\ntau : input rank-1 array('D') with bounds (k)\nc : input rank-2 array('D') with bounds (ldc,n)\nlwork : input int\n\nOther Parameters\n----------------\noverwrite_c : input int, optional\n    Default: 0\n\nReturns\n-------\ncq : rank-2 array('D') with bounds (ldc,n) and c storage\nwork : rank-1 array('D') with bounds (MAX(lwork,1))\ninfo : int\n"
    pass

