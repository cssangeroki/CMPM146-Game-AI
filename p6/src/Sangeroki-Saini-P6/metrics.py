ó
âh²_c           @   s   d  d l  Z  d  d l Z d  d l Z d   Z e d k r e j d Z e e d   Z	 e	 j
   Z Wd QXe e  e e d  f GHe e  GHn  d S(   iÿÿÿÿNc   6         sÒ	  t     t   d   t    d } d } t d d d d d d d	 d
 d d d d d d d g    f d     xh t  d d d  D]P }  | | d k s¾  | | d k r    | d |  r | } Pq q Wd8 d9 d: d; d< g d= d> d? d@ dA g dB dC dD dE dF g dG dH dI dJ dK dL dM dN dO dP dQ dR g dS dT dU dV dW dX dY dZ d[ d\ d] d^ g g  g  } x  D] } | d g } x` t d t  |   D]I } | j | | d | | d d | | d | | d d f  q¤W| j |  q{W|  t           f d    } d }	 t j | | d f  f d!   | |	  }
 d"   |
 D } xb t   D]T } d# } xE t   D]7 } | | f  k rº| d 7} q|  | | 7} qWq|WxH |
 D]@ } | | d j g  | d D] } | d | d f ^ qú qÛW| }
 i  } t   } x< t   D]. }   d | d k rA| j |  qAqAWx'|
 D]} i g  d$ 6g  d% 6| | <xþ |
 | D]ò } d  d } t } x­ | D]¥ } | d d& k  r   | d d | d  rt } qÂ| rÂ d 7 t } xM t d  D]< } | d |  k  r$| d | | k r$| d 7} Pq$q$WqÂqÂW| | d$ j   | | d% j |  q£WqzWd } d } d } t	 d'  } xs | D]k } | | k  rÝ| } n  x* | | d$ D] } | | 7} | d 7} qìWx  | | d% D] } | | 7} qWqÂWd } d } x | D] } x> | | d$ D]. } | t	 |  t	 |  } | | | 7} qYWx> | | d% D]. } | t	 |  t	 |  } | | | 7} qWqDW  } d } d } d } d }  d }! d }" d }# x" D]}$ | |$ j
 d(  7} | |$ j
 d  |$ j
 d(  |$ j
 d)  |$ j
 d  7} | |$ j
 d  |$ j
 d  7} |  |$ j
 d  7}  |! |$ j
 d)  |$ j
 d  |$ j
 d*  7}! |# |$ j
 d*  7}# |" |$ j
 d  |$ j
 d  |$ j
 d  |$ j
 d  |$ j
 d*  |$ j
 d  7}" qWt	 t     t	 |  }% t	 |  t	 |  }& t	 |  t	 |  }' t	 |  t	 |   t	 |  t	 |!  t	 |  }( | |# d+ d+ |! t  |  }) g  }* g  }+ d } x t   D] } d } | d k r`xa  | D]R },   |,  rO   | d |  rO|* j |  |+ j |  n  | d 7} qWn  | d 7} qäWt j |*  }- t j |+  }. d d, l m }/ |/ j |- |.  \ }0 }1 }2 }3 }4 t j |2  }5 t  |
  d k rv	i  d- 6|% d. 6|& d/ 6|' d0 6|( d1 6|) d2 6t	 |  t	 |  d% 6t	 |  t	 |  d$ 6t	 |  t	 |  d3 6t	 |  t	 |  d4 6|5 d5 6d6 d7 6Si  d- 6|% d. 6d d/ 6|' d0 6|( d1 6|) d2 6d d% 6d d$ 6d d3 6d d4 6|5 d5 6d d7 6Sd  S(_   Ni    i   t   Xt   Qt   St   ?t   Bt   bt   [t   ]t   Tt   |t   <t   >t   vt   ft   mc            s
   |    k S(   N(    (   t   tile(   t   solids(    s;   /Users/claudiosangeroki/ucscfiles/cmpm146/p6/src/metrics.pyt   isSolid   s    iÿÿÿÿt   -t   *i   iþÿÿÿiýÿÿÿiüÿÿÿi   i   i   i   i   i   c            sv  |  d } |  d }   j  |  d |  d f  |  d |  d d f } g  } | d  k ra g  S|  d d k r¸|  d d } |  d } | t  |  k  r¸|  d |  d  | | d  k p|  d |  d  | | d d k  p|  d  | | d d k  rµ   |  d  | | d |  d |  d  | | d  rµ| j | d |  d |  d  | | d |  d  | | d | | |  d f g  qµq¸n     | d | d  rh|  d d  k  r8   |  d |  d d  r8| j | d |  d d |  d d f g  n  |  d d d k r   |  d |  d d  r| j | d |  d d |  d d f g  n  xÓt t    D]²} d } |  d  | | d  k pø|  d  | | d d k  r   |  d  | | d |  d  | | d  r| j | | d |  d  | | d |  d  | | d | | d f g  n  |  d  | | d d k  pË|  d  | | d d k  r¯   |  d  | | d |  d  | | d  r¯| j | | d |  d  | | d |  d  | | d | | d f g  q¯q¯Wn
| j | d |  d |  d d d f g  |  d d  k  r|  d d  k  r   |  d d |  d d  r| j | d |  d d |  d d d f g  n  |  d d d k r   |  d d |  d d  r| j | d |  d d |  d d d f g  qn  |  d d  k  rr|  d d  k  r   |  d d |  d d  r| j | d |  d d |  d d d f g  n  |  d d d k rr   |  d d |  d d  rr| j | d |  d d |  d d d f g  qrn  | S(   Ni    i   i   iÿÿÿÿi   i   gffffffö?(   t   addt   lent   appendt   range(   t   post   distt   belowt	   neighborst   iit   jump(   R   t   jumpst   levelStrt   maxXt   maxYt   visited(    s;   /Users/claudiosangeroki/ucscfiles/cmpm146/p6/src/metrics.pyt   getNeighborsF   sH    


¶c5/5/~U~\,93969396c            s   |  d   d k S(   Ni    i   (    (   R   (   R    (    s;   /Users/claudiosangeroki/ucscfiles/cmpm146/p6/src/metrics.pyt   <lambda>r   t    c         S   s   i  |  ] } g  | d   q S(   i    (    (   t   .0t   path(    (    s;   /Users/claudiosangeroki/ucscfiles/cmpm146/p6/src/metrics.pys
   <dictcomp>t   s   	 R%   R   t   meaningfulJumpsi   t   inft   Et   ot   Mg      à?(   t   statst   lengtht   negativeSpacet   pathPercentaget   emptyPercentaget   decorationPercentaget   leniencyt   meaningfulJumpVariancet   jumpVariancet	   linearityg      ð?t   solvability(   i    iÿÿÿÿ(   i    iþÿÿÿ(   i   iýÿÿÿ(   i   iüÿÿÿ(   i    iüÿÿÿ(   i    iÿÿÿÿ(   i    iþÿÿÿ(   i    iýÿÿÿ(   i    iüÿÿÿ(   i   iüÿÿÿ(   i   iÿÿÿÿ(   i   iþÿÿÿ(   i   iýÿÿÿ(   i   iüÿÿÿ(   i   iüÿÿÿ(   i   iÿÿÿÿ(   i   iþÿÿÿ(   i   iþÿÿÿ(   i   iýÿÿÿ(   i   iýÿÿÿ(   i   iüÿÿÿ(   i   iüÿÿÿ(   i   iýÿÿÿ(   i   iýÿÿÿ(   i   iýÿÿÿ(   i   iþÿÿÿ(   i   iÿÿÿÿ(   i   iÿÿÿÿ(   i   iþÿÿÿ(   i   iþÿÿÿ(   i   iýÿÿÿ(   i   iýÿÿÿ(   i   iüÿÿÿ(   i   iüÿÿÿ(   i   iüÿÿÿ(   i   iýÿÿÿ(   i   iýÿÿÿ(   i   iþÿÿÿ(   i   iÿÿÿÿ(   R   t   setR   R   t   pathfindingt   dijkstras_shortest_pathR   t   Truet   Falset   floatt   countt   npt   arrayt   scipyR-   t
   linregresst   abs(6   R   t   curXt   curYt   yyt	   jumpDiffsR   t   jumpDiffR   R#   t
   subOptimalt   pathst   pathDictt   st   xxR'   t   pt	   pathStatst   gapst
   pathLengthR(   t   onGroundt
   totalJumpst   totalMeaningfulJumpst	   pathcountt   smallestR5   R4   t   tempt	   totalSizet   enemiest   pipest   emptyt	   breakablet   rewardst   solidt   powerupst   rowR/   R0   R1   R2   R3   t   solidXt   solidYt   ct   xt   yR-   t   slopet	   interceptt   r_valuet   p_valuet   std_errR6   (    (   R   R   R   R    R!   R   R"   s;   /Users/claudiosangeroki/ucscfiles/cmpm146/p6/src/metrics.pyt   metrics   sf   	9@G	**>	0	
(
	

: -X4 %!
t   __main__i   t   ri    (   R9   t   numpyR?   t   sysRk   t   __name__t   argvt   namet   opent   openFilet	   readlinest   linesR   (    (    (    s;   /Users/claudiosangeroki/ucscfiles/cmpm146/p6/src/metrics.pyt   <module>   s   	ô