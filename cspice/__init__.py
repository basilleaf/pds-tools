# This file was automatically generated by SWIG (http://www.swig.org).
# Version 1.3.40
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.
# This file is compatible with both classic and new-style classes.

from sys import version_info
if version_info >= (2,6,0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_cspice', [dirname(__file__)])
        except ImportError:
            import _cspice
            return _cspice
        if fp is not None:
            try:
                _mod = imp.load_module('_cspice', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _cspice = swig_import_helper()
    del swig_import_helper
else:
    import _cspice
del version_info
try:
    _swig_property = property
except NameError:
    pass # Python < 2.2 doesn't have 'property'.
def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static) or hasattr(self,name):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError(name)

def _swig_repr(self):
    try: strthis = "proxy of " + self.this.__repr__()
    except: strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0



def axisar(*args):
  """axisar(double axis, double angle)"""
  return _cspice.axisar(*args)

def b1900():
  """b1900() -> double"""
  return _cspice.b1900()

def b1950():
  """b1950() -> double"""
  return _cspice.b1950()

def bodc2n(*args):
  """bodc2n(int code)"""
  return _cspice.bodc2n(*args)

def boddef(*args):
  """boddef(char CONST_STRING, int code)"""
  return _cspice.boddef(*args)

def bodfnd(*args):
  """bodfnd(int body, char CONST_STRING) -> int"""
  return _cspice.bodfnd(*args)

def bodn2c(*args):
  """bodn2c(char CONST_STRING)"""
  return _cspice.bodn2c(*args)

def bods2c(*args):
  """bods2c(char CONST_STRING)"""
  return _cspice.bods2c(*args)

def bodvcd(*args):
  """bodvcd(int bodyid, char CONST_STRING)"""
  return _cspice.bodvcd(*args)

def bodvrd(*args):
  """bodvrd(char arg0, char CONST_STRING)"""
  return _cspice.bodvrd(*args)

def cgv2el(*args):
  """cgv2el(double center, double vec1, double vec2)"""
  return _cspice.cgv2el(*args)

def cidfrm(*args):
  """cidfrm(int cent)"""
  return _cspice.cidfrm(*args)

def ckcov(*args):
  """
    ckcov(char ck, int idcode, int needav, char level, double tol, 
        char timsys)
    """
  return _cspice.ckcov(*args)

def ckgp(*args):
  """ckgp(int inst, double sclkdp, double tol, char CONST_STRING)"""
  return _cspice.ckgp(*args)

def ckgpav(*args):
  """ckgpav(int inst, double sclkdp, double tol, char CONST_STRING)"""
  return _cspice.ckgpav(*args)

def ckobj(*args):
  """ckobj(char ck)"""
  return _cspice.ckobj(*args)

def clight():
  """clight() -> double"""
  return _cspice.clight()

def clpool():
  """clpool()"""
  return _cspice.clpool()

def cnmfrm(*args):
  """cnmfrm(char cname)"""
  return _cspice.cnmfrm(*args)

def conics(*args):
  """conics(double elts, double et)"""
  return _cspice.conics(*args)

def convrt(*args):
  """convrt(double x, char arg1, char CONST_STRING)"""
  return _cspice.convrt(*args)

def cyllat(*args):
  """cyllat(double r, double lonc, double z)"""
  return _cspice.cyllat(*args)

def cylrec(*args):
  """cylrec(double r, double lon, double z)"""
  return _cspice.cylrec(*args)

def cylsph(*args):
  """cylsph(double r, double lonc, double z)"""
  return _cspice.cylsph(*args)

def dcyldr(*args):
  """dcyldr(double x, double y, double z)"""
  return _cspice.dcyldr(*args)

def deltet(*args):
  """deltet(double epoch, char CONST_STRING)"""
  return _cspice.deltet(*args)

def det(*args):
  """det(double m1) -> double"""
  return _cspice.det(*args)

def dgeodr(*args):
  """dgeodr(double x, double y, double z, double re, double f)"""
  return _cspice.dgeodr(*args)

def diags2(*args):
  """diags2(double symmat)"""
  return _cspice.diags2(*args)

def dlatdr(*args):
  """dlatdr(double x, double y, double z)"""
  return _cspice.dlatdr(*args)

def dpgrdr(*args):
  """
    dpgrdr(char CONST_STRING, double x, double y, double z, double re, 
        double f)
    """
  return _cspice.dpgrdr(*args)

def dpmax():
  """dpmax() -> double"""
  return _cspice.dpmax()

def dpmin():
  """dpmin() -> double"""
  return _cspice.dpmin()

def dpr():
  """dpr() -> double"""
  return _cspice.dpr()

def drdcyl(*args):
  """drdcyl(double r, double lon, double z)"""
  return _cspice.drdcyl(*args)

def drdgeo(*args):
  """drdgeo(double lon, double lat, double alt, double re, double f)"""
  return _cspice.drdgeo(*args)

def drdlat(*args):
  """drdlat(double r, double lon, double lat)"""
  return _cspice.drdlat(*args)

def drdpgr(*args):
  """
    drdpgr(char CONST_STRING, double lon, double lat, double alt, 
        double re, double f)
    """
  return _cspice.drdpgr(*args)

def drdsph(*args):
  """drdsph(double r, double colat, double lon)"""
  return _cspice.drdsph(*args)

def dsphdr(*args):
  """dsphdr(double x, double y, double z)"""
  return _cspice.dsphdr(*args)

def dtpool(*args):
  """dtpool(char CONST_STRING)"""
  return _cspice.dtpool(*args)

def dvdot(*args):
  """dvdot(double s1, double s2) -> double"""
  return _cspice.dvdot(*args)

def dvhat(*args):
  """dvhat(double s1)"""
  return _cspice.dvhat(*args)

def edlimb(*args):
  """edlimb(double a, double b, double c, double viewpt)"""
  return _cspice.edlimb(*args)

def el2cgv(*args):
  """el2cgv(double ellipse)"""
  return _cspice.el2cgv(*args)

def erract(*args):
  """erract(char CONST_STRING, int lenout)"""
  return _cspice.erract(*args)

def errch(*args):
  """errch(char arg0, char CONST_STRING)"""
  return _cspice.errch(*args)

def errdev(*args):
  """errdev(char CONST_STRING, int lenout)"""
  return _cspice.errdev(*args)

def errdp(*args):
  """errdp(char CONST_STRING, double number)"""
  return _cspice.errdp(*args)

def errint(*args):
  """errint(char CONST_STRING, int number)"""
  return _cspice.errint(*args)

def errprt(*args):
  """errprt(char CONST_STRING, int lenout)"""
  return _cspice.errprt(*args)

def et2lst(*args):
  """
    et2lst(double et, int body, double lon, char type, int hr, 
        int mn, int sc)
    """
  return _cspice.et2lst(*args)

def et2utc(*args):
  """et2utc(double et, char CONST_STRING, int prec)"""
  return _cspice.et2utc(*args)

def etcal(*args):
  """etcal(double et)"""
  return _cspice.etcal(*args)

def eul2m(*args):
  """
    eul2m(double angle3, double angle2, double angle1, int axis3, 
        int axis2, int axis1)
    """
  return _cspice.eul2m(*args)

def eul2xf(*args):
  """eul2xf(double eulang, int axisa, int axisb, int axisc)"""
  return _cspice.eul2xf(*args)

def expool(*args):
  """expool(char CONST_STRING)"""
  return _cspice.expool(*args)

def failed():
  """failed() -> int"""
  return _cspice.failed()

def frame(*args):
  """frame(double xin)"""
  return _cspice.frame(*args)

def frinfo(*args):
  """frinfo(int frcode)"""
  return _cspice.frinfo(*args)

def frmchg(*args):
  """frmchg(int frame1, int frame2, double et)"""
  return _cspice.frmchg(*args)

def frmchg_(*args):
  """frmchg_(int frame1, int frame2, double et, double xform)"""
  return _cspice.frmchg_(*args)

def frmnam(*args):
  """frmnam(int frcode)"""
  return _cspice.frmnam(*args)

def furnsh(*args):
  """furnsh(char CONST_STRING)"""
  return _cspice.furnsh(*args)

def gcpool(*args):
  """gcpool(char CONST_STRING, int start)"""
  return _cspice.gcpool(*args)

def gdpool(*args):
  """gdpool(char CONST_STRING, int start)"""
  return _cspice.gdpool(*args)

def georec(*args):
  """georec(double lon, double lat, double alt, double re, double f)"""
  return _cspice.georec(*args)

def getfov(*args):
  """getfov(int instid, int room, int n, double bounds)"""
  return _cspice.getfov(*args)

def getmsg(*args):
  """getmsg(char CONST_STRING)"""
  return _cspice.getmsg(*args)

def gipool(*args):
  """gipool(char CONST_STRING, int start)"""
  return _cspice.gipool(*args)

def gnpool(*args):
  """gnpool(char CONST_STRING, int start)"""
  return _cspice.gnpool(*args)

def halfpi():
  """halfpi() -> double"""
  return _cspice.halfpi()

def ident():
  """ident()"""
  return _cspice.ident()

def illum(*args):
  """
    illum(char arg0, double et, char arg2, char CONST_STRING, 
        double spoint)
    """
  return _cspice.illum(*args)

def inedpl(*args):
  """inedpl(double a, double b, double c, double plane)"""
  return _cspice.inedpl(*args)

def inelpl(*args):
  """inelpl(double ellipse, double plane)"""
  return _cspice.inelpl(*args)

def inrypl(*args):
  """inrypl(double vertex, double dir, double plane)"""
  return _cspice.inrypl(*args)

def intmax():
  """intmax() -> int"""
  return _cspice.intmax()

def intmin():
  """intmin() -> int"""
  return _cspice.intmin()

def invert(*args):
  """invert(double m1)"""
  return _cspice.invert(*args)

def invort(*args):
  """invort(double m)"""
  return _cspice.invort(*args)

def isrot(*args):
  """isrot(double m, double ntol, double dtol) -> int"""
  return _cspice.isrot(*args)

def j1900():
  """j1900() -> double"""
  return _cspice.j1900()

def j1950():
  """j1950() -> double"""
  return _cspice.j1950()

def j2000():
  """j2000() -> double"""
  return _cspice.j2000()

def j2100():
  """j2100() -> double"""
  return _cspice.j2100()

def jyear():
  """jyear() -> double"""
  return _cspice.jyear()

def latcyl(*args):
  """latcyl(double radius, double lon, double lat)"""
  return _cspice.latcyl(*args)

def latrec(*args):
  """latrec(double radius, double longitude, double latitude)"""
  return _cspice.latrec(*args)

def latsph(*args):
  """latsph(double radius, double lon, double lat)"""
  return _cspice.latsph(*args)

def ldpool(*args):
  """ldpool(char CONST_STRING)"""
  return _cspice.ldpool(*args)

def lspcn(*args):
  """lspcn(char arg0, double et, char CONST_STRING) -> double"""
  return _cspice.lspcn(*args)

def ltime(*args):
  """ltime(double etobs, int obs, char CONST_STRING, int targ)"""
  return _cspice.ltime(*args)

def m2eul(*args):
  """m2eul(double rin, int axis3, int axis2, int axis1)"""
  return _cspice.m2eul(*args)

def m2q(*args):
  """m2q(double rin)"""
  return _cspice.m2q(*args)

def mequ(*args):
  """mequ(double m1)"""
  return _cspice.mequ(*args)

def mequg(*args):
  """mequg(double m1, double mout, int nr_vout, int nc_vout)"""
  return _cspice.mequg(*args)

def mtxm(*args):
  """mtxm(double m1, double m2)"""
  return _cspice.mtxm(*args)

def mtxmg(*args):
  """mtxmg(double m1, double m2)"""
  return _cspice.mtxmg(*args)

def mtxv(*args):
  """mtxv(double m1, double vin)"""
  return _cspice.mtxv(*args)

def mtxvg(*args):
  """mtxvg(double m1, double v2)"""
  return _cspice.mtxvg(*args)

def mxm(*args):
  """mxm(double m1, double m2)"""
  return _cspice.mxm(*args)

def mxmg(*args):
  """mxmg(double m1, double m2)"""
  return _cspice.mxmg(*args)

def mxmt(*args):
  """mxmt(double m1, double m2)"""
  return _cspice.mxmt(*args)

def mxmtg(*args):
  """mxmtg(double m1, double m2)"""
  return _cspice.mxmtg(*args)

def mxv(*args):
  """mxv(double m1, double vin)"""
  return _cspice.mxv(*args)

def mxvg(*args):
  """mxvg(double m1, double v2)"""
  return _cspice.mxvg(*args)

def namfrm(*args):
  """namfrm(char CONST_STRING)"""
  return _cspice.namfrm(*args)

def nearpt(*args):
  """nearpt(double positn, double a, double b, double c)"""
  return _cspice.nearpt(*args)

def npedln(*args):
  """npedln(double a, double b, double c, double linept, double linedr)"""
  return _cspice.npedln(*args)

def npelpt(*args):
  """npelpt(double point)"""
  return _cspice.npelpt(*args)

def nplnpt(*args):
  """nplnpt(double linpt, double lindir, double point)"""
  return _cspice.nplnpt(*args)

def nvc2pl(*args):
  """nvc2pl(double normal, double constant)"""
  return _cspice.nvc2pl(*args)

def nvp2pl(*args):
  """nvp2pl(double normal, double point)"""
  return _cspice.nvp2pl(*args)

def oscelt(*args):
  """oscelt(double state, double et, double mu)"""
  return _cspice.oscelt(*args)

def pcpool(*args):
  """pcpool(char CONST_STRING, int n)"""
  return _cspice.pcpool(*args)

def pdpool(*args):
  """pdpool(char CONST_STRING, int n)"""
  return _cspice.pdpool(*args)

def pgrrec(*args):
  """
    pgrrec(char CONST_STRING, double lon, double lat, double alt, 
        double re, double f)
    """
  return _cspice.pgrrec(*args)

def pi():
  """pi() -> double"""
  return _cspice.pi()

def pipool(*args):
  """pipool(char CONST_STRING, int n)"""
  return _cspice.pipool(*args)

def pjelpl(*args):
  """pjelpl(double elin, double plane)"""
  return _cspice.pjelpl(*args)

def pl2nvc(*args):
  """pl2nvc(double plane, double normal)"""
  return _cspice.pl2nvc(*args)

def pl2nvp(*args):
  """pl2nvp(double plane)"""
  return _cspice.pl2nvp(*args)

def pl2psv(*args):
  """pl2psv(double plane)"""
  return _cspice.pl2psv(*args)

def prop2b(*args):
  """prop2b(double gm, double pvinit, double dt)"""
  return _cspice.prop2b(*args)

def psv2pl(*args):
  """psv2pl(double point, double span1, double span2)"""
  return _cspice.psv2pl(*args)

def pxform(*args):
  """pxform(char arg0, char CONST_STRING, double et)"""
  return _cspice.pxform(*args)

def q2m(*args):
  """q2m(double qin)"""
  return _cspice.q2m(*args)

def qdq2av(*args):
  """qdq2av(double qin, double dq)"""
  return _cspice.qdq2av(*args)

def qxq(*args):
  """qxq(double q1, double q2)"""
  return _cspice.qxq(*args)

def radrec(*args):
  """radrec(double range, double ra, double dec)"""
  return _cspice.radrec(*args)

def rav2xf(*args):
  """rav2xf(double rot, double av)"""
  return _cspice.rav2xf(*args)

def raxisa(*args):
  """raxisa(double matrix)"""
  return _cspice.raxisa(*args)

def reccyl(*args):
  """reccyl(double rectan1)"""
  return _cspice.reccyl(*args)

def recgeo(*args):
  """recgeo(double rectan1, double re, double f)"""
  return _cspice.recgeo(*args)

def reclat(*args):
  """reclat(double rectan1)"""
  return _cspice.reclat(*args)

def recpgr(*args):
  """recpgr(char CONST_STRING, double rectan1, double re, double f)"""
  return _cspice.recpgr(*args)

def recrad(*args):
  """recrad(double rectan)"""
  return _cspice.recrad(*args)

def recsph(*args):
  """recsph(double rectan)"""
  return _cspice.recsph(*args)

def refchg(*args):
  """refchg(int frame1, int frame2, double et)"""
  return _cspice.refchg(*args)

def refchg_(*args):
  """refchg_(int frame1, int frame2, double et, double rotate)"""
  return _cspice.refchg_(*args)

def repmc(*args):
  """repmc(char arg0, char arg1, char CONST_STRING)"""
  return _cspice.repmc(*args)

def repmct(*args):
  """repmct(char arg0, char CONST_STRING, int value, char IN_STRING)"""
  return _cspice.repmct(*args)

def repmd(*args):
  """repmd(char arg0, char CONST_STRING, double value, int sigdig)"""
  return _cspice.repmd(*args)

def repmf(*args):
  """
    repmf(char arg0, char CONST_STRING, double value, int sigdig, 
        char format)
    """
  return _cspice.repmf(*args)

def repmi(*args):
  """
    repmi(char arg0, char CONST_STRING, int value, int lenout, 
        char out)
    """
  return _cspice.repmi(*args)

def repmot(*args):
  """repmot(char arg0, char CONST_STRING, int value, char IN_STRING)"""
  return _cspice.repmot(*args)

def reset():
  """reset()"""
  return _cspice.reset()

def rotate(*args):
  """rotate(double angle, int iaxis)"""
  return _cspice.rotate(*args)

def rotmat(*args):
  """rotmat(double m1, double angle, int iaxis)"""
  return _cspice.rotmat(*args)

def rotvec(*args):
  """rotvec(double v1, double angle, int iaxis)"""
  return _cspice.rotvec(*args)

def rpd():
  """rpd() -> double"""
  return _cspice.rpd()

def rquad(*args):
  """rquad(double a, double b, double c)"""
  return _cspice.rquad(*args)

def saelgv(*args):
  """saelgv(double vec1, double vec2)"""
  return _cspice.saelgv(*args)

def scdecd(*args):
  """scdecd(int sc, double sclkdp)"""
  return _cspice.scdecd(*args)

def sce2c(*args):
  """sce2c(int sc, double et)"""
  return _cspice.sce2c(*args)

def sce2s(*args):
  """sce2s(int sc, double et)"""
  return _cspice.sce2s(*args)

def sce2t(*args):
  """sce2t(int sc, double et)"""
  return _cspice.sce2t(*args)

def scencd(*args):
  """scencd(int sc, char CONST_STRING)"""
  return _cspice.scencd(*args)

def scfmt(*args):
  """scfmt(int sc, double ticks)"""
  return _cspice.scfmt(*args)

def scpart(*args):
  """scpart(int sc)"""
  return _cspice.scpart(*args)

def scs2e(*args):
  """scs2e(int sc, char CONST_STRING)"""
  return _cspice.scs2e(*args)

def sct2e(*args):
  """sct2e(int sc, double sclkdp)"""
  return _cspice.sct2e(*args)

def sctiks(*args):
  """sctiks(int sc, char CONST_STRING)"""
  return _cspice.sctiks(*args)

def setmsg(*args):
  """setmsg(char CONST_STRING)"""
  return _cspice.setmsg(*args)

def sigerr(*args):
  """sigerr(char CONST_STRING)"""
  return _cspice.sigerr(*args)

def spd():
  """spd() -> double"""
  return _cspice.spd()

def sphcyl(*args):
  """sphcyl(double radius, double colat, double slon)"""
  return _cspice.sphcyl(*args)

def sphlat(*args):
  """sphlat(double r, double colat, double lons)"""
  return _cspice.sphlat(*args)

def sphrec(*args):
  """sphrec(double r, double colat, double lon)"""
  return _cspice.sphrec(*args)

def spkapo(*args):
  """spkapo(int targ, double et, char arg2, double sobs, char CONST_STRING)"""
  return _cspice.spkapo(*args)

def spkapp(*args):
  """spkapp(int targ, double et, char arg2, double sobs, char CONST_STRING)"""
  return _cspice.spkapp(*args)

def spkcov(*args):
  """spkcov(char spk, int idcode)"""
  return _cspice.spkcov(*args)

def spkez(*args):
  """
    spkez(int targ, double et, char arg2, char CONST_STRING, 
        int obs)
    """
  return _cspice.spkez(*args)

def spkez_vector(*args):
  """spkez_vector(int targ, double et, char ref, char abcorr, int obs)"""
  return _cspice.spkez_vector(*args)

def spkezp(*args):
  """
    spkezp(int targ, double et, char arg2, char CONST_STRING, 
        int obs)
    """
  return _cspice.spkezp(*args)

def spkezr(*args):
  """spkezr(char arg0, double et, char arg2, char arg3, char CONST_STRING)"""
  return _cspice.spkezr(*args)

def spkgeo(*args):
  """spkgeo(int targ, double et, char CONST_STRING, int obs)"""
  return _cspice.spkgeo(*args)

def spkgps(*args):
  """spkgps(int targ, double et, char CONST_STRING, int obs)"""
  return _cspice.spkgps(*args)

def spkobj(*args):
  """spkobj(char spk)"""
  return _cspice.spkobj(*args)

def spkpos(*args):
  """spkpos(char arg0, double et, char arg2, char arg3, char CONST_STRING)"""
  return _cspice.spkpos(*args)

def spkssb(*args):
  """spkssb(int targ, double et, char CONST_STRING)"""
  return _cspice.spkssb(*args)

def srfrec(*args):
  """srfrec(int body, double longitude, double latitude)"""
  return _cspice.srfrec(*args)

def srfxpt(*args):
  """
    srfxpt(char arg0, char arg1, double et, char arg3, char arg4, 
        char CONST_STRING, double dvec)
    """
  return _cspice.srfxpt(*args)

def stcf01(*args):
  """
    stcf01(char catnam, double westra, double eastra, double sthdec, 
        double nthdec)
    """
  return _cspice.stcf01(*args)

def stcg01(*args):
  """stcg01(int index)"""
  return _cspice.stcg01(*args)

def stcl01(*args):
  """stcl01(char catfnm)"""
  return _cspice.stcl01(*args)

def stelab(*args):
  """stelab(double pobj, double vobs)"""
  return _cspice.stelab(*args)

def stpool(*args):
  """stpool(char arg0, int nth, char CONST_STRING)"""
  return _cspice.stpool(*args)

def str2et(*args):
  """str2et(char CONST_STRING)"""
  return _cspice.str2et(*args)

def subpt(*args):
  """subpt(char arg0, char arg1, double et, char arg3, char CONST_STRING)"""
  return _cspice.subpt(*args)

def subsol(*args):
  """subsol(char arg0, char arg1, double et, char arg3, char CONST_STRING)"""
  return _cspice.subsol(*args)

def surfnm(*args):
  """surfnm(double a, double b, double c, double point)"""
  return _cspice.surfnm(*args)

def surfpt(*args):
  """surfpt(double positn, double u, double a, double b, double c)"""
  return _cspice.surfpt(*args)

def sxform(*args):
  """sxform(char arg0, char CONST_STRING, double et)"""
  return _cspice.sxform(*args)

def sxform_vector(*args):
  """sxform_vector(char _from, char to, double et)"""
  return _cspice.sxform_vector(*args)

def timdef(*args):
  """timdef(char arg0, char CONST_STRING, int lenout)"""
  return _cspice.timdef(*args)

def timout(*args):
  """timout(double et, char CONST_STRING)"""
  return _cspice.timout(*args)

def tipbod(*args):
  """tipbod(char CONST_STRING, int body, double et)"""
  return _cspice.tipbod(*args)

def tisbod(*args):
  """tisbod(char CONST_STRING, int body, double et)"""
  return _cspice.tisbod(*args)

def tkvrsn(*args):
  """tkvrsn(char CONST_STRING) -> char"""
  return _cspice.tkvrsn(*args)

def tparse(*args):
  """tparse(char string)"""
  return _cspice.tparse(*args)

def tpictr(*args):
  """tpictr(char sample)"""
  return _cspice.tpictr(*args)

def trace(*args):
  """trace(double matrix) -> double"""
  return _cspice.trace(*args)

def trcoff():
  """trcoff()"""
  return _cspice.trcoff()

def tsetyr(*args):
  """tsetyr(int year)"""
  return _cspice.tsetyr(*args)

def twopi():
  """twopi() -> double"""
  return _cspice.twopi()

def twovec(*args):
  """twovec(double axdef, int indexa, double plndef, int indexp)"""
  return _cspice.twovec(*args)

def tyear():
  """tyear() -> double"""
  return _cspice.tyear()

def ucrss(*args):
  """ucrss(double v1, double v2)"""
  return _cspice.ucrss(*args)

def unitim(*args):
  """unitim(double epoch, char arg1, char CONST_STRING) -> double"""
  return _cspice.unitim(*args)

def unload(*args):
  """unload(char CONST_STRING)"""
  return _cspice.unload(*args)

def unorm(*args):
  """unorm(double v1)"""
  return _cspice.unorm(*args)

def unormg(*args):
  """unormg(double v1)"""
  return _cspice.unormg(*args)

def utc2et(*args):
  """utc2et(char CONST_STRING)"""
  return _cspice.utc2et(*args)

def vadd(*args):
  """vadd(double v1, double v2)"""
  return _cspice.vadd(*args)

def vaddg(*args):
  """vaddg(double v1, double v2)"""
  return _cspice.vaddg(*args)

def vcrss(*args):
  """vcrss(double v1, double v2)"""
  return _cspice.vcrss(*args)

def vdist(*args):
  """vdist(double v1, double v2) -> double"""
  return _cspice.vdist(*args)

def vdistg(*args):
  """vdistg(double v1, double v2) -> double"""
  return _cspice.vdistg(*args)

def vdot(*args):
  """vdot(double v1, double v2) -> double"""
  return _cspice.vdot(*args)

def vdotg(*args):
  """vdotg(double v1, double v2) -> double"""
  return _cspice.vdotg(*args)

def vequ(*args):
  """vequ(double vin)"""
  return _cspice.vequ(*args)

def vequg(*args):
  """vequg(double v1)"""
  return _cspice.vequg(*args)

def vhat(*args):
  """vhat(double v1)"""
  return _cspice.vhat(*args)

def vhatg(*args):
  """vhatg(double v1)"""
  return _cspice.vhatg(*args)

def vlcom3(*args):
  """
    vlcom3(double a, double v1, double b, double v2, double c, 
        double v3)
    """
  return _cspice.vlcom3(*args)

def vlcom(*args):
  """vlcom(double a, double v1, double b, double v2)"""
  return _cspice.vlcom(*args)

def vlcomg(*args):
  """vlcomg(double a, double v1, double b, double v2)"""
  return _cspice.vlcomg(*args)

def vminug(*args):
  """vminug(double v1)"""
  return _cspice.vminug(*args)

def vminus(*args):
  """vminus(double v1)"""
  return _cspice.vminus(*args)

def vnorm(*args):
  """vnorm(double v1) -> double"""
  return _cspice.vnorm(*args)

def vnormg(*args):
  """vnormg(double v1) -> double"""
  return _cspice.vnormg(*args)

def vpack(*args):
  """vpack(double x, double y, double z)"""
  return _cspice.vpack(*args)

def vperp(*args):
  """vperp(double a, double b)"""
  return _cspice.vperp(*args)

def vprjp(*args):
  """vprjp(double vin, double plane)"""
  return _cspice.vprjp(*args)

def vprjpi(*args):
  """vprjpi(double vin, double projpl, double invpl)"""
  return _cspice.vprjpi(*args)

def vproj(*args):
  """vproj(double a, double b)"""
  return _cspice.vproj(*args)

def vrel(*args):
  """vrel(double v1, double v2) -> double"""
  return _cspice.vrel(*args)

def vrelg(*args):
  """vrelg(double v1, double v2) -> double"""
  return _cspice.vrelg(*args)

def vrotv(*args):
  """vrotv(double v, double axis, double theta)"""
  return _cspice.vrotv(*args)

def vscl(*args):
  """vscl(double s, double v1)"""
  return _cspice.vscl(*args)

def vsclg(*args):
  """vsclg(double s, double v1)"""
  return _cspice.vsclg(*args)

def vsep(*args):
  """vsep(double v1, double v2) -> double"""
  return _cspice.vsep(*args)

def vsepg(*args):
  """vsepg(double v1, double v2) -> double"""
  return _cspice.vsepg(*args)

def vsub(*args):
  """vsub(double v1, double v2)"""
  return _cspice.vsub(*args)

def vsubg(*args):
  """vsubg(double v1, double v2)"""
  return _cspice.vsubg(*args)

def vtmv(*args):
  """vtmv(double v1, double matrix) -> double"""
  return _cspice.vtmv(*args)

def vtmvg(*args):
  """vtmvg(double v1, double matrix, double v2) -> double"""
  return _cspice.vtmvg(*args)

def vupack(*args):
  """vupack(double v)"""
  return _cspice.vupack(*args)

def vzero(*args):
  """vzero(double v) -> int"""
  return _cspice.vzero(*args)

def vzerog(*args):
  """vzerog(double v) -> int"""
  return _cspice.vzerog(*args)

def xf2eul(*args):
  """xf2eul(double xform, int axisa, int axisb, int axisc)"""
  return _cspice.xf2eul(*args)

def xf2rav(*args):
  """xf2rav(double xform)"""
  return _cspice.xf2rav(*args)

def xpose6(*args):
  """xpose6(double m1)"""
  return _cspice.xpose6(*args)

def xpose(*args):
  """xpose(double m1)"""
  return _cspice.xpose(*args)

def xposeg(*args):
  """xposeg(double matrix)"""
  return _cspice.xposeg(*args)


