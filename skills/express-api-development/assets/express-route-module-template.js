const express = require("express");

const router = express.Router();

// Validation middleware should run before handlers
router.post("/resources", validateCreateResource, async (req, res, next) => {
  try {
    const result = await createResource(req.body, req.context);
    return res.status(201).json(result);
  } catch (error) {
    return next(error);
  }
});

module.exports = router;
