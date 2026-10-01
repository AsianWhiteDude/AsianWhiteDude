# Profile artwork

The profile introduces Mikhail at a glance and gives direct access to his resume and contacts. Career history belongs in `resume/`; project catalogs and activity counters are deliberately absent from the profile README.

## Art direction

A dimensional sculpture of glass, aluminium and light is paired with an original shared-stem MK monogram and Space Grotesk typography. The dark artwork is an intentional poster within both GitHub themes. The mobile version has its own composition rather than shrinking desktop text.

The sculpture was generated for this profile using the built-in ImageGen tool. The WebP source is stored here; vector typography and the monogram are authored in `build_assets.py`. No third-party image service, analytics widget, API token, workflow or scheduled refresh is required. The light animates once for 3.8 seconds. Reduced-motion readers receive separate still images.

## Rebuild

Use Python 3 with `fonttools` from `requirements.txt`, then run:

```sh
python3 design/build_assets.py
```

The script writes `assets/profile/*.svg`. Images embed the local artwork and convert the bundled font's outlines to SVG paths, so the browser needs no external font or image requests. The font's license is retained in `fonts/OFL.txt`.

## References

These informed the composition and separation of identity from career detail; no artwork or source code was copied:

- [Nikita Fedorov](https://github.com/nikitafedorov008): one dominant atmospheric image.
- [Andrii Drok](https://github.com/andriidrok1): a personal visual signature.
- [Alexandre Sanlim](https://github.com/alexandresanlim): compact introduction with deeper details kept separate.
- [Reza Shakeri](https://github.com/rzashakeri): immediate contact actions and a moving focal point.
- [lowlighter](https://github.com/lowlighter): a consistent authored visual system.
- [3D contribution artwork](https://github.com/yoshi389111/github-profile-3d-contrib): dimensionality and finite SVG motion; no contribution data is used here.

Two alternatives were considered: a purely typographic technical poster, and a lavender vector MK sculpture. The glass/aluminium composition was selected for its stronger visual identity, with the custom MK mark retained as the personal signature.

Trade-off: artwork cannot reflow like text, so mobile gets a dedicated layout. The short introduction and links remain native HTML, and the artwork includes a meaningful alternative description.
