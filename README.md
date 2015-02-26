Swede NG
========

SwedeNG is a heavily work-in-progress re-implementation of the `swede` tool that
was written in 2012 during the standarization of DANE (DNS-Based Authentication
of Named Entities, [rfc6698](https://tools.ietf.org/html/rfc6698)). It was
created as a proof-of-concept tool with the intention of keeping it up to date.
However, due to time constraints and a lack of good coding styles, this never
happened.

SwedeNG will be fully rewritten from scratch, have tests and will consist of a
library called `swede` and several tools. Planned tools for now are:

 * `tlsa` - Generate and verify TLSA records (the 'old' swede)
 * as-yet unnamed tool for DANE with S/MIME
 * as-yet unnamed tool for DANE with OpenPGP

SwedeNG will be versioned according to [semantic versioning](http://semver.org).
