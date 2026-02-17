# Image Hardening Checklist

- [ ] Multi-stage build used where applicable.
- [ ] Runtime image contains only required artifacts.
- [ ] Non-root user configured in final stage.
- [ ] Package/dependency versions are controlled.
- [ ] Secrets are not copied into image layers.
